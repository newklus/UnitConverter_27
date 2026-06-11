# TDD RED — `unit_convert` 전용

`.cursorrules` · `tests/test_unit_convert.py` · `src/unit_convert.py` 계약을 따른다. **RED는 tests/만 수정.**

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: RED
```

한 번에 **RED만**. GREEN·REFACTOR·`src/`·`UnitConverter.py` 작업 금지.

---

## RED 목표

`unit_convert(user_input: float)`에 대한 **실패하는 pytest**를 추가·갱신한다.

- 스텁(`...`) → 기대: `status: "incomplete"` 또는 assertion **실패**
- 구현 후 GREEN 전까지: **의도된 실패**가 pytest에 드러나야 함
- 대상 파일: **`tests/test_unit_convert.py`만** (CLI TC·`test_unit_converter.py`는 RED 범위 밖)

---

## AAA 절차

각 테스트 함수는 **Arrange → Act → Assert** 순서로 작성.

| 단계 | 내용 |
|------|------|
| **Arrange** | `user_input` · golden 3줄(`.cursorrules` 표시 golden) · 기대 `status` / `failed_lines` |
| **Act** | `result = unit_convert(user_input)` |
| **Assert** | `result["status"]` · `result["failed_lines"]` — **완화·skip·xfail 금지** |

**표시 golden (meter, 1자리):**

- `2.5` → `pass`, 3줄: `2.5 meter = 2.5 meter` · `2.5 meter = 8.2 feet` · `2.5 meter = 2.7 yard`
- `1` → `pass`, 3줄: `1 meter = 1.0 meter` · `1 meter = 3.3 feet` · `1 meter = 1.1 yard`
- `-1` → `fail` (음수 입력 검증)

정밀 TC(8.2021, 0.9144)는 **RED에 넣지 않음** — 표시 TC와 분리.

---

## pytest 예시

```python
from unit_convert import unit_convert


def test_unit_convert_meter_2_5_pass():
    # Arrange
    user_input = 2.5
    expected_lines = [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2 feet",
        "2.5 meter = 2.7 yard",
    ]

    # Act
    result = unit_convert(user_input)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []
    assert result["lines"] == expected_lines  # 구현 시 반환 필드명은 tests SSOT


def test_unit_convert_negative_fail():
    # Arrange
    user_input = -1

    # Act
    result = unit_convert(user_input)

    # Assert
    assert result["status"] == "fail"
    assert len(result["failed_lines"]) > 0


def test_unit_convert_stub_incomplete():
    # Arrange — 스텁 단계 RED
    user_input = 2.5

    # Act
    result = unit_convert(user_input)

    # Assert
    assert result["status"] == "incomplete"
```

RED 확인 명령:

```bash
pytest tests/test_unit_convert.py -v
```

**기대:** 최소 1개 **FAILED** 또는 **incomplete assertion FAILED** (의도된 RED).

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` · `UnitConverter.py` 수정 | GREEN Phase |
| assert 완화 · `@pytest.mark.skip` · `xfail` | 실패 숨김 |
| golden·기대값 낮추기 | RED 목적 훼손 |
| 정밀 TC를 표시 TC와 혼합 | Rule ⑤ |
| CLI·OCP·YAML 작업 | 범위 밖 |

---

## 보고 형식 (RED 완료 시)

```markdown
Phase: RED

## 추가·수정 테스트
- `test_...` — (한 줄 설명)

## pytest 결과
- 명령: `pytest tests/test_unit_convert.py -v`
- 결과: FAILED n / passed m (의도된 실패 테스트명 나열)

## 다음
- GREEN: `src/unit_convert.py` 최소 구현
```

---

## 참고

- SSOT: `tests/` golden > `.cursorrules`
- API: `{ "status": "pass"|"fail"|"incomplete", "failed_lines": [...] }`
- `lines` 등 추가 반환 필드는 **tests에서 먼저 고정** (RED가 계약 주도)
