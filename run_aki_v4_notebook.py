from __future__ import annotations

import json
import sys
import time
import traceback
from pathlib import Path

import nbformat


NOTEBOOK = Path("aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb")
LOG_PATH = Path("aki_v4_execution.log")
PROGRESS_PATH = Path("aki_v4_execution_progress.json")


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data: str) -> None:
        for stream in self.streams:
            stream.write(data)
            stream.flush()

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def clean_notebook_code(source: str) -> str:
    """Drop IPython magics so the notebook can run in a plain Python process."""
    cleaned = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("%") or stripped.startswith("!"):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def display(obj=None, *args, **kwargs) -> None:
    if obj is not None:
        print(obj)


def write_progress(cell_index: int, status: str, started: float, error: str | None = None) -> None:
    payload = {
        "notebook": str(NOTEBOOK.resolve()),
        "cell_index": cell_index,
        "status": status,
        "elapsed_seconds": round(time.time() - started, 2),
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "error": error,
    }
    PROGRESS_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    if not NOTEBOOK.exists():
        raise FileNotFoundError(NOTEBOOK)
    nb = nbformat.read(NOTEBOOK, as_version=4)
    # Run all executable workflow cells except package-install magics.
    code_cell_indices = [
        i for i, cell in enumerate(nb.cells)
        if cell.cell_type == "code" and i != 3
    ]
    namespace = {"display": display}
    started = time.time()
    with LOG_PATH.open("a", encoding="utf-8", buffering=1) as log_f:
        tee_out = Tee(sys.__stdout__, log_f)
        tee_err = Tee(sys.__stderr__, log_f)
        old_out, old_err = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = tee_out, tee_err
        try:
            print(f"AKI v4 notebook run started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Notebook: {NOTEBOOK.resolve()}")
            for idx in code_cell_indices:
                source = clean_notebook_code(nb.cells[idx].source)
                if not source.strip():
                    continue
                print(f"\n===== START cell {idx} at {time.strftime('%Y-%m-%d %H:%M:%S')} =====")
                write_progress(idx, "running", started)
                cell_started = time.time()
                try:
                    exec(compile(source, f"notebook_cell_{idx}", "exec"), namespace)
                except Exception as exc:
                    err = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
                    print(err)
                    write_progress(idx, "failed", started, error=str(exc))
                    return 1
                print(f"===== END cell {idx}; cell_elapsed={time.time() - cell_started:.1f}s =====")
            write_progress(code_cell_indices[-1], "completed", started)
            print(f"AKI v4 notebook run completed in {time.time() - started:.1f}s")
            return 0
        finally:
            sys.stdout, sys.stderr = old_out, old_err


if __name__ == "__main__":
    raise SystemExit(main())
