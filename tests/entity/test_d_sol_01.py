from entity.solve import solve_step_a
from tests._approval import assert_matches_golden


def test_d_sol_01_step_a_success(grid_g1):
    # Given — grid_g1 (4×4 row-major, blank 2개)
    expected_blanks = [5, 15]

    # When — solve step A (grid 검증)
    result = solve_step_a(grid_g1)

    # Then
    assert result == {
        "status": "success",
        "step": "a",
        "blanks": expected_blanks,
    }


def test_d_sol_01_golden(grid_g1):
    # Given — grid_g1 (고정 fixture)
    # When
    result = solve_step_a(grid_g1)
    actual = (
        f"status: {result['status']}\n"
        f"step: {result['step']}\n"
        f"blanks: {result['blanks']}\n"
    )

    # Then — Approval
    assert_matches_golden(actual, "d_sol_01")
