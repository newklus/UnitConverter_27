from entity.constants import BLANK_VALUE, GRID_G1_BLANK_COUNT, GRID_SIZE
from entity.validation import all_line_sums, all_lines_match_magic_sum


def solve_step_a(grid):
    if len(grid) != GRID_SIZE:
        return {"status": "fail", "step": "a", "reason": "invalid_grid_size"}
    blanks = [i for i, v in enumerate(grid) if v == BLANK_VALUE]
    if len(blanks) != GRID_G1_BLANK_COUNT:
        return {"status": "fail", "step": "a", "reason": "invalid_blank_count"}
    return {"status": "success", "step": "a", "blanks": blanks}


def validate_ten_line_sums(grid):
    if len(grid) != GRID_SIZE:
        return {"status": "fail", "step": "b", "reason": "invalid_grid_size"}
    line_sums = all_line_sums(grid)
    if not all_lines_match_magic_sum(grid):
        return {
            "status": "fail",
            "step": "b",
            "reason": "sum_mismatch",
            "line_sums": line_sums,
        }
    return {"status": "success", "step": "b", "line_sums": line_sums}
