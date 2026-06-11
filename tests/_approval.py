import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).parent / "golden"


def assert_matches_golden(actual: str, golden_id: str) -> None:
    """Compare actual output to tests/golden/{golden_id}.approved.txt."""
    golden_path = GOLDEN_DIR / f"{golden_id}.approved.txt"
    update = os.environ.get("UPDATE_GOLDEN") == "1"

    if update or not golden_path.exists():
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual, encoding="utf-8")
        if update:
            return

    expected = golden_path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(
            f"Golden mismatch: {golden_path}\n"
            f"--- expected\n{expected!r}\n--- actual\n{actual!r}"
        )
