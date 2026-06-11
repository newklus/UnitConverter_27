# GREEN Minimal — ARRR R단계 (Respond = GREEN)

**RED 1묶음당 최소 구현** — 해당 Test ID만 GREEN. **1커밋 = 1 RED 묶음** (커밋은 사용자 요청 시만).

**unit_converter-tdd** Skill이 있으면 **자동 따름** (상수·계층·네이밍).

SSOT: `tests/` golden **>** `docs/PRD.md` **>** `.cursorrules` **>** `README.md` · 상수는 **`constants.py`**

**Skill:** `unit_converter-tdd` — constants · 계층 · 1묶음 GREEN.

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
| **Phase** | `green` | ARRR R = Respond (최소 구현) |
| **Layer** | `entity` \| `boundary` | Logic 기본 = `entity` |
| **Track** | `Logic` \| `UI` | boundary GREEN → `Layer: boundary` · CLI/`UnitConverter.py` |

**한 번에 green-minimal만.** REFACTOR · **다른 Test ID 동시 GREEN** 금지.

---

## 역할 · 범위

| 항목 | 내용 |
|------|------|
| **선행** | `/tdd-red` 완료 — 대상 Test ID **assert RED** (또는 skeleton → `/tdd-red` 후) |
| **산출물** | `src/` **최소** production 코드 + tests에서 **`pytest.fail` 제거·assert 유지** |
| **범위** | **이번 RED 묶음 Test ID 1개(또는 플랜에 묶인 동일 묶음)** 만 |
| **다음 단계** | 다음 RED 묶음 또는 `/refactor` (별도 Command · 본 Phase 아님) |

---

## 자동 추출 (추가 입력 없음)

`/green-minimal` **단독** 입력 시 **직전 RED·채팅**에서 추출. **확인 질문 금지.**

| 추출 항목 | 출처 |
|-----------|------|
| **Test ID** | red-test-plan · tdd-red · skeleton fail 메시지 |
| **대상 함수·파일** | Track B · `tests/` import |
| **golden·계약** | tests assert · `.cursorrules` |
| **RED 묶음** | 이번에 GREEN할 ID **1묶음만** |

---

## 절차 (순서 고정)

| # | 단계 | 작업 |
|---|------|------|
| 1 | **RED 재확인** | 대상 Test ID만 pytest → **FAILED** (의도된 RED) 확인 |
| 2 | **constants SSOT** | 매직넘버·하드코딩 **금지** — `src/constants.py`에 상수 정의·import |
| 3 | **src/ 최소 구현** | **이번 Test ID 통과에 필요한 최소** 코드만 (다른 ID 선행 구현 금지) |
| 4 | **tests 정리** | `pytest.fail("RED: …")` **제거** · `/tdd-red` assert **유지·복원** (완화 금지) |
| 5 | **PASS 확인** | 대상 테스트 **PASSED** + **회귀** (같은 파일·전체 `pytest`) |
| 6 | **보고** | PASS Test ID · 변경 파일 · 회귀 결과 |

### RED 재확인 명령 (예)

```bash
pytest tests/test_unit_convert.py::test_t2_meter_2_5_display_pass -v
```

**기대:** FAILED (assert 또는 `pytest.fail`).

### PASS 확인 명령 (예)

```bash
# 단일 Test ID
pytest tests/test_unit_convert.py::test_t2_meter_2_5_display_pass -v

# 파일 전체 (동일 RED 파일 회귀)
pytest tests/test_unit_convert.py -v
```

---

## constants.py SSOT

| 규칙 | 내용 |
|------|------|
| **금지** | 함수 본문·테스트에 `3.28084`, `1.09361` 등 **리터럴 반복** |
| **허용** | `src/constants.py` 한 곳 정의 → `src/`에서 **import** |
| **UnitConverter_27** | `METER_TO_FEET`, `METER_TO_YARD`, `DISPLAY_DECIMALS` 등 |

- constants **없으면 GREEN 중 생성** (`src/constants.py`).
- tests는 **golden 값** SSOT; production은 **constants + 계산**만.

---

## ECB · E001~E005 · 계층

| 규칙 | entity (Logic) |
|------|----------------|
| **E001~E005** | `raise` · `return` 에러코드 **금지** — fail은 `{status, failed_lines}` dict (UnitConverter) 또는 Skill 계약 |
| **ECB emit** | GREEN minimal에서 **이벤트 버스·핸들러 설계·코드 없음** |
| **import 금지** | **entity** → `boundary` · `control` · CLI · I/O 레이어 **import 금지** |
| **boundary GREEN** | `UnitConverter.py` · `capsys` TC — **entity 로직 mock 금지**, entity 함수 **호출** |

---

## 구현 원칙 (최소)

```python
# ✅ 이번 Test ID (예: T1 음수)만
if user_input < 0:
    return {"status": "fail", "failed_lines": [...]}

# ❌ 같은 커밋에서 meter:2.5 golden까지 한꺼번에 (다른 RED 묶음)
```

- **YAGNI:** 다음 RED를 위해 미리 API 확장·리팩터 **하지 않음**.
- **회귀:** 기존 PASS TC 깨지면 **즉시 수정** (assert 완화로 해결 **금지**).

---

## 금지

| 금지 | 이유 |
|------|------|
| **이번 RED 묶음 외 Test ID** 동시 GREEN | 1묶음 = 1 최소 diff |
| **REFACTOR** | 별도 Phase |
| assert 완화 · skip · xfail | GREEN = tests SSOT 충족 |
| 하드코딩 · 매직넘버 | `constants.py` SSOT |
| E001~E005 raise/return | ECB 이후 · dict 계약 우선 |
| entity → boundary/control import | 계층 역전 |
| OCP · YAML · GUI | `.cursorrules` 범위 밖 |
| **git commit / push** (사용자 미요청) | `.cursorrules` |

---

## git (사용자 요청 시만)

| 규칙 | 내용 |
|------|------|
| **1커밋 = 1 RED 묶음** | Test ID 단위 메시지 (예: `green: T1 negative input fail`) |
| **포함** | `src/` · 해당 tests assert 정리 |
| **미요청** | `git commit` · `push` **실행하지 않음** |

---

## 보고 형식 (GREEN 완료 시)

```markdown
Phase: green
Layer: entity
Track: Logic

## PASS
| Test ID | 함수 | 결과 |
|---------|------|------|
| T1 | test_t1_negative_input_fail | PASSED |

## pytest
- 단일: `pytest tests/test_unit_convert.py::test_t1_negative_input_fail -v` → 1 passed
- 파일: `pytest tests/test_unit_convert.py -v` → n passed, m failed (다른 RED 묶음은 여전히 FAILED 가능)

## 변경 파일
- src/unit_convert.py
- src/constants.py (신규 시)
- tests/... (pytest.fail 제거 시)

## 회귀
- (없음) 또는 — 깨진 TC명 · **즉시 수정** 내역

## 다음
- 다음 RED 묶음 `/tdd-red` 또는 `/green-minimal`
```

**회귀 실패 시:** 보고 **전에** 수정·재실행 — assert 완화 **금지**.

---

## Command 흐름 (ARRR 실습)

```
/red-test-plan → /red-skeleton → /tdd-red → /green-minimal (본 Command)
→ /golden-master → /refactor-smell → /refactor-safe → /export-session
```

---

## UnitConverter_27 참고

| RED 묶음 | 최소 GREEN 범위 |
|----------|-----------------|
| **T1** | `user_input < 0` → `status: fail`, `failed_lines` |
| **T2** | `unit_convert(2.5)` → pass 3줄 (1자리) — **T1과 별도 묶음이면 T1 선행 GREEN 금지(이미 PASS면 유지)** |
| **T3** | `unit_convert(1)` → pass 3줄 golden |
| **U-IN-01/02** | `Layer: boundary` · `UnitConverter.py` 입력 검증만 |

- `pythonpath = ["src"]` — `from unit_convert import unit_convert`
- 표시 golden: `.cursorrules` Rule ③ · ⑦

---

## Skill 참조

> **unit_converter-tdd** Skill이 있으면 **자동 따름** — `src/constants.py` · 계층 import 규칙 · Test ID별 최소 GREEN 범위.

Skill 없음 → 본 Command + `tests/` assert + `.cursorrules`.
