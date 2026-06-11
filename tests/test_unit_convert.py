from unit_convert import unit_convert


def test_t1_negative_input_fail():
    # Arrange — 0보다 작은 meter 값 → 변환 결과도 음수 구간, 입력 검증 fail
    user_input = -1
    expected_failed_lines = [
        {"reason": "negative_input", "user_input": -1},
    ]

    # Act
    result = unit_convert(user_input)

    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == expected_failed_lines
