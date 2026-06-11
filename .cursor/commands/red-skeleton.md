# RED Skeleton — ARRR A단계 (RED ④)

**/red-test-plan** 설계표(C2C · Track B · 테스트 플랜) 기준으로 **`pytest.fail` 스켈레톤만** 작성한다.

**unit_converter-tdd** Skill이 있으면 **자동 따름** (픽스처·상수·grid 규칙·네이밍).

SSOT: `/red-test-plan` 산출 **>** `docs/PRD.md` **>** `.cursorrules` **>** `README.md`

**Skill:** `unit_converter-tdd` — grid_g1 · constants · Test ID 네이밍.

---

## Phase 선언 (필수)

응답 **첫 두 줄**:

```
Phase: red
Layer: entity
Track: Logic
```

| 필드 | 값 | 비고 |
|------|-----|------|
| **Phase** | `red` | ARRR A = RED ④ (스켈레톤) |
| **Layer** | `entity` \| `boundary` | Logic 기본 = `entity` |
| **Track** | `Logic` \| `UI` | boundary Track → `Layer: boundary` |

**Track A (boundary):** `Layer: boundary` · `Track: UI` — `capsys`/`monkeypatch` Arrange만 추가, **Then은 동일하게 `pytest.fail` 한 줄**.

---

## 역할 · 범위

| 항목 | 내용 |
|------|------|
| **선행** | `/red-test-plan` 완료 · " `/red-skeleton` 으로 넘길 준비됐다` " |
| **산출물** | `tests/` 테스트 함수 **골격** — AAA 주석 + **`pytest.fail` Then 1줄** |
| **다음 단계** | `/tdd-red` — `pytest.fail` → **실제 assert** 본문 (RED 본문) |

**한 번에 red-skeleton만.** GREEN · REFACTOR · assert golden 본문 · production 코드 금지.

---

## 자동 추출 (추가 입력 없음)

`/red-skeleton` **단독** 입력 시 **직전 `/red-test-plan`·채팅**에서 추출. **확인 질문 금지.**

| 추출 항목 | 출처 |
|-----------|------|
| **Test ID** | red-test-plan C2C · Track B (예: `D-LOC-01`, `U-IN-01`) |
| **함수명** | 플랜 블록 3 · `test_{test_id_snake}` |
| **파일 경로** | 플랜 블록 3 |
| **Given / When** | C2C Rule3 |
| **fail 메시지 Then** | Track B Expected RED Failure 요약 |

---

## AAA + pytest.fail 규칙

| 단계 | 작성 |
|------|------|
| **Arrange** | `# Given — …` · 플랜·픽스처·상수 import |
| **Act** | `# When — …` · 호출 **1줄** (또는 skeleton 단계에서 **생략** 가능) |
| **Assert (Then)** | **`pytest.fail("RED: {Test ID} — …")` 한 줄만** |

### Then 금지 · 허용

| | |
|--|--|
| **허용** | `pytest.fail("RED: D-LOC-01 — blank coords row-major 미구현")` |
| **금지** | `assert …` 본문 · `pass` · `return` · 통과 더미 |
| **금지** | `@pytest.mark.skip` · `xfail` · `pytest.raises` assert |

**의미:** skeleton RED = **항상 FAIL** — `/tdd-red`에서 fail을 assert로 **교체**.

---

## 상수 · conftest (entity · Magic Square)

**픽스처 데이터만** — Domain 로직 import 금지 (`src/` production 함수 호출 금지는 skeleton에서도 When 생략 시 해당 없음).

### 상수 import

```python
from entity.constants import MAGIC_SUM, GRID_SIZE, BLANK_COUNT
# MAGIC_SUM=34 · GRID_SIZE=16(4×4) · BLANK_COUNT=4 — Skill/entity/constants.py SSOT
```

- **`src/` 수정 금지** — `entity/constants.py`는 **이미 존재**할 때만 import.
- UnitConverter_27 등 상수 없는 프로젝트: `.cursorrules` golden·리터럴을 Given에만 기술 (constants import **생략**).

### conftest — `tests/conftest.py`

| 픽스처 | 내용 |
|--------|------|
| **`grid_g1`** | 4×4 row-major · **0(빈칸) 2개** · unit_converter-tdd Skill SSOT |

```python
import pytest

@pytest.fixture
def grid_g1():
    """4×4 row-major, two blanks (0). Skill SSOT."""
    return [
        16,  3,  2, 13,
         5, 10, 11,  8,
         9,  6,  7, 12,
         4, 15, 14,  0,  # 예: (3,3)=0 + 한 칸 더 0 — Skill 정의 따름
    ]
```

- skeleton **생성 시** `tests/conftest.py`에 `grid_g1` **없으면 추가** (tests/만).
- UnitConverter: `grid_g1` **불필요** — conftest 수정 **하지 않음**.

---

## 템플릿 예시 — `test_d_loc_01_blank_coords_row_major`

Magic Square · Logic · entity · RED 묶음 `D-LOC-01`:

```python
import pytest

from entity.constants import MAGIC_SUM, GRID_SIZE, BLANK_COUNT


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given — 4×4 grid, row-major, two blanks (0); MAGIC_SUM=34
    assert len(grid_g1) == GRID_SIZE
    blank_indices = [i for i, v in enumerate(grid_g1) if v == 0]
    assert len(blank_indices) == 2  # fixture sanity only (skeleton 허용)

    # When — blank_coords_row_major(grid) 호출 (GREEN 전)

    # Then
    pytest.fail("RED: D-LOC-01 — blank coords row-major 미구현")
```

**UnitConverter_27 대응 예** (`D-LOC-01` · `unit_convert` · conftest 없음):

```python
import pytest


def test_d_loc_01_meter_2_5_display_pass():
    # Given — user_input=2.5, golden 3줄 (Rule ③)
    user_input = 2.5

    # When — unit_convert(user_input)

    # Then
    pytest.fail("RED: D-LOC-01 — meter 2.5 표시 3줄 pass 미구현")
```

---

## 작성 절차

1. `/red-test-plan` RED 묶음 Test ID 목록 확인
2. 플랜 **파일·함수명**에 맞춰 `tests/`에 skeleton 함수 **추가** (기존 assert TC **덮어쓰지 않음** — `/tdd-red` 전 단계)
3. AAA 주석 + **`pytest.fail` Then 1줄**
4. Magic Square: `entity.constants` import · `grid_g1` fixture 연결
5. **`pytest` 실행** → 전부 **FAILED** (fail 메시지) 확인
6. 보고 형식 출력

---

## pytest 실행 · 보고 (필수)

```bash
pytest tests/ -v -k "{test_id_snake or red_bundle}"
```

### 보고 형식

```markdown
Phase: red
Layer: entity
Track: Logic

## pytest.fail 스켈레톤
| Test ID | 함수 | FAIL 한 줄 |
|---------|------|-------------|
| D-LOC-01 | test_d_loc_01_blank_coords_row_major | RED: D-LOC-01 — blank coords row-major 미구현 |

## pytest 결과
- 명령: `pytest tests/... -v`
- 결과: FAILED n (전부 의도된 pytest.fail)

## 변경 파일 (tests/만)
- tests/test_....py
- tests/conftest.py (grid_g1 추가 시만)

## 다음
- `/tdd-red` — pytest.fail → assert 본문
```

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` · `UnitConverter.py` · `entity/` **로직** 수정 | GREEN |
| assert golden **본문** | `/tdd-red` |
| `pass` · no-op · 통과 더미 | skeleton = 항상 FAIL |
| skip · xfail | 실패 숨김 |
| GREEN · REFACTOR | Phase red skeleton only |
| red-test-plan **없이** Test ID 임의 발명 | SSOT |

---

## Command 흐름 (ARRR 실습)

```
/red-test-plan → /red-skeleton (본 Command) → /tdd-red
→ /green-minimal → /golden-master → /refactor-smell → /refactor-safe → /export-session
```

---

## Skill 참조

> **unit_converter-tdd** Skill(`.cursor/skills/` 또는 프로젝트 Skill)이 있으면 **자동 따름** — `grid_g1` 정의 · `entity/constants.py` · Test ID 네이밍 · row-major 규칙.

Skill 없음 → 본 Command + `/red-test-plan` + `.cursorrules`만 사용.

---

## 참고

- skeleton의 fixture sanity `assert`(예: `len(grid_g1)==16`)는 **Given 검증용** — **Then assert golden 아님**
- 기존 `test_t1_negative_input_fail` 등 **assert TC**는 skeleton이 **교체하지 않음** — 새 Test ID만 추가
- `pyproject.toml` `pythonpath = ["src"]` — UnitConverter는 `from unit_convert import …` (entity 패키지 없음)
