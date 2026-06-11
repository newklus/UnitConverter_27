# Golden Master — Approval Test (GREEN PASS 후)

**GREEN PASS**된 Test ID에 대해 **Golden Master(Approval Test)** 파일을 구축·검증한다.

**unit_converter-tdd** Skill이 있으면 **자동 따름** (golden 경로·포맷·Test ID 네이밍).

SSOT: `tests/` assert golden **>** `tests/golden/*.approved.txt` **>** `docs/PRD.md` **>** `.cursorrules`

**Skill:** `unit_converter-tdd` — golden_id · 포맷 · `UPDATE_GOLDEN` 절차.

---

## Phase 선언 (필수)

응답 **첫 두 줄**:

```
Phase: green
Layer: entity
Track: Logic
```

| 필드 | 값 | 비고 |
|------|-----|------|
| **Phase** | `green` | GREEN PASS **이후** Approval Test 단계 |
| **Layer** | `entity` \| `boundary` | Logic 기본 = `entity` |
| **Track** | `Logic` \| `UI` | boundary → CLI stdout golden |

**한 번에 golden-master만.** production 리팩터 · assert 완화 · golden 수동 편집 금지.

---

## 역할 · 범위

| 항목 | 내용 |
|------|------|
| **전제** | 대상 Test ID **pytest PASS** (`/green-minimal` 완료) |
| **산출물** | `tests/_approval.py` · `tests/golden/{id}.approved.txt` · approval TC 연결 |
| **목적** | 구현 출력을 **고정 baseline**과 diff 없이 일치 — 회귀·승인 테스트 |
| **다음 단계** | 다음 RED 묶음 또는 REFACTOR (golden **유지** — 구현만 baseline에 맞춤) |

---

## 자동 추출 (추가 입력 없음)

`/golden-master` **단독** 입력 시 **직전 GREEN·채팅**에서 추출. **확인 질문 금지.**

| 추출 항목 | 출처 |
|-----------|------|
| **Test ID** | green-minimal 보고 · PASS TC (예: `T1`, `T2`) |
| **golden id** | Test ID → snake: `d_loc_01`, `t1` |
| **출력 캡처** | tests assert · API 반환 · CLI stdout |
| **입력값** | Given — **고정** (랜덤은 `seed` 고정 후 literal SSOT) |

---

## 절차 (순서 고정)

| # | 단계 | 작업 |
|---|------|------|
| 0 | **PASS 확인** | 대상 Test ID pytest → **PASSED** (미통과 시 golden-master **중단**) |
| 1 | **`tests/_approval.py`** | `assert_matches_golden` **없으면 생성** (공통 헬퍼) |
| 2 | **golden 연결** | `tests/golden/{id}.approved.txt` 경로·TC에서 참조 |
| 3 | **baseline 생성** | `UPDATE_GOLDEN=1 pytest …` — **코드 출력**으로 파일 생성 |
| 4 | **matched 검증** | `UPDATE_GOLDEN` **없이** pytest → **matched** 확인 |
| 5 | **보고** | golden 경로 · matched 여부 · diff 요약 |

---

## 1. `tests/_approval.py`

**없으면 생성.** 프로젝트 공통 Approval 헬퍼.

```python
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
```

| 규칙 | 내용 |
|------|------|
| **UPDATE_GOLDEN=1** | baseline **덮어쓰기** (코드 출력만) |
| **파일 없음** | 첫 실행 시 자동 생성 후 **재실행**으로 matched 확인 |
| **인코딩** | UTF-8 · `\n` 줄바꿈 고정 |

---

## 2. golden 파일 연결

| 항목 | 규칙 |
|------|------|
| **경로** | `tests/golden/{golden_id}.approved.txt` |
| **golden_id** | Test ID snake lower: `T1` → `t1` · `T2` → `t2` |
| **TC 위치** | 기존 PASS TC 옆 또는 `tests/test_approval_{id}.py` |
| **캡처 대상** | dict → **고정 포맷 문자열** · CLI → stdout strip |

### 출력 포맷 (고정)

| Track | 포맷 |
|-------|------|
| **Logic · dict** | `status: …\nfailed_lines: …\nlines:\n  …` (키 순·indent SSOT) |
| **boundary · CLI** | 오류/성공 메시지 **한 줄씩** · trailing newline 일관 |
| **에러 코드** | `{status, failed_lines}` 문자열 — **E001~E005 emit 금지** · reason 키 고정 |

**입력값 고정:** approval TC의 Given은 **literal** — `random` 사용 시 `seed` + 주석으로 SSOT 명시.

---

## 3. baseline 생성 — `UPDATE_GOLDEN=1`

```bash
# 단일 Test ID approval
UPDATE_GOLDEN=1 pytest tests/test_unit_convert.py::test_t1_golden -v

# golden id 묶음
UPDATE_GOLDEN=1 pytest tests/ -k "golden and t1" -v
```

- **기대:** golden 파일 **생성·갱신** · pytest **PASSED** (update 모드는 diff 검사 skip)
- baseline은 **항상 production 코드 실행 결과** — **수동 편집 금지**

---

## 4. matched 확인 (UPDATE_GOLDEN 없음)

```bash
pytest tests/test_unit_convert.py::test_t1_golden -v
pytest tests/ -v -k golden
```

- **기대:** **PASSED** = matched
- **FAILED** = `AssertionError: Golden mismatch` — diff 요약 보고 · **golden 수동 수정 금지** → **구현 또는 포맷 함수** 수정

---

## TC 예시 — T1

```python
actual = f"status: {result['status']}\nfailed_lines: {result['failed_lines']}\n"
assert_matches_golden(actual, "t1")
```

---

## golden 수동 편집 · 우회 금지

| 금지 | 이유 |
|------|------|
| `.approved.txt` **직접 수정**으로 pytest 통과 | baseline 신뢰 붕괴 |
| assert 완화 · skip · xfail | SSOT 훼손 |
| UPDATE_GOLDEN 없이 golden 삭제 후 재생성 | 절차 3→4 생략 |
| 임의 포맷·입력값 변경 | diff 재현 불가 |

**허용:** `UPDATE_GOLDEN=1` + **코드 출력 변경** 후 baseline **재생성** (의도적 계약 변경 시만).

---

## 금지

| 금지 | 이유 |
|------|------|
| PASS **전** golden-master | 전제 미충족 |
| `src/` **기능 확장** (golden 통과용) | `/green-minimal` 범위 |
| golden 수동 편집 우회 | Approval Test 목적 |
| E001~E005 · ECB emit | dict/문자열 계약만 |
| OCP · YAML · GUI | 범위 밖 |
| **git commit / push** (사용자 미요청) | `.cursorrules` |

---

## 보고 형식 (완료 시)

```markdown
Phase: green
Layer: entity
Track: Logic

## Golden Master
| Test ID | golden 경로 | matched |
|---------|-------------|---------|
| T1 | tests/golden/t1.approved.txt | ✅ matched |

## pytest
- 생성: `UPDATE_GOLDEN=1 pytest …::test_t1_golden -v` → passed
- 검증: `pytest …::test_t1_golden -v` → passed (UPDATE_GOLDEN 없음)

## diff 요약
- (matched) diff 없음
- (mismatch 시) expected vs actual 1~3줄 요약 · **수정 방향: src/ 또는 format 함수**

## 변경 파일
- tests/_approval.py (신규 시)
- tests/golden/t1.approved.txt
- tests/test_unit_convert.py (approval TC 추가)

## 다음
- 다음 Test ID `/golden-master` 또는 RED 묶음
```

**mismatch 시:** golden **편집하지 않고** 구현·포맷 수정 후 절차 4 재실행.

---

## Command 흐름 (ARRR 실습)

```
/red-test-plan → … → /green-minimal → /golden-master (본 Command)
→ /refactor-smell → /refactor-safe → /export-session
```

---

## UnitConverter_27 참고

| Test ID | golden_id | 캡처 내용 |
|---------|-----------|-----------|
| T1 | `t1` | `status: fail` · `failed_lines: [{'reason': 'negative_input', …}]` |
| T2 | `t2` | pass 3줄 표시 golden (Rule ③) |
| T3 | `t3` | `meter:1` 3줄 golden |

- 표시 golden 1자리: `.cursorrules` Rule ⑦
- CLI boundary: stdout 전체 · 오류 메시지 SSOT (`UnitConverter.py` 표)

---

## Skill 참조

> **unit_converter-tdd** Skill이 있으면 **자동 따름** — golden 경로 · dict/stdout 포맷 · Test ID ↔ golden_id 매핑.

Skill 없음 → 본 Command + PASS TC assert + `.cursorrules`.
