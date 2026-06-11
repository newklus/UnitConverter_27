---
name: unit_converter-tdd
description: >-
  Dual-Track ARRR TDD for UnitConverter_27 (meter/feet/yard, unit_convert API).
  Use when Phase is red, green, or refactor; when running /red-test-plan,
  /red-skeleton, /tdd-red, /green-minimal, /golden-master, /refactor-smell,
  /refactor-safe; or when the user mentions TDD, RED, GREEN, REFACTOR,
  Dual-Track, C2C, pytest.fail, unit_convert, or UnitConverter CLI.
disable-model-invocation: true
---

# UnitConverter TDD

Dual-Track ARRR + strict TDD for **UnitConverter_27**. Commands: `.cursor/commands/`.

**SSOT:** `tests/` golden **>** `docs/PRD.md` **>** `.cursorrules` **>** `README.md`  
(PRD 없으면 Rule ①~⑧·API·golden 표를 FR로 매핑)

**단독 입력:** `/슬래시명` 만 → 채팅·SSOT 자동 추출 · **확인 질문 금지**

---

## 1. ARRR ↔ TDD

| ARRR | TDD | Commands | 산출 |
|------|-----|----------|------|
| **Ask** | **RED** | `/red-test-plan` → `/red-skeleton` → `/tdd-red` | C2C · `pytest.fail` · assert |
| **Respond** | **GREEN** | `/green-minimal` → `/golden-master` | 최소 구현 · Approval |
| **Refine** | **REFACTOR** | `/refactor-smell` → `/refactor-safe` | 스멜 · Budget 리팩터 |

**한 턴 = 한 Phase.** RED→tests/만 · GREEN→assert 유지 · REFACTOR→동작·golden 불변.

---

## 2. Phase 선언

| Phase | 응답 첫 줄 |
|-------|------------|
| **red** | `Phase: red` · `Layer: entity\|boundary` · `Track: Logic\|UI` |
| **green** | `Phase: green` · Layer · Track |
| **refactor** | `Phase: refactor` · `Scope: src/ tests/` · `Track: Logic+UI` |

- Logic: `unit_convert` · `src/` — `Layer: entity`
- CLI: `UnitConverter.py` — `Layer: boundary` · `Track: UI`

---

## 3. C2C Rule 1~3

| Rule | 내용 |
|------|------|
| **1** | FR-ID + 한 줄 (PRD 또는 `.cursorrules` Rule/API) |
| **2** | To-Do **1개** (동사) |
| **3** | Test ID · Given · When · Then |

---

## 4. RED 금지

| 금지 |
|------|
| `src/` · `UnitConverter.py` 수정 |
| skip · xfail · assert 완화 |
| Logic Track **Domain mock** |
| E001~E005 · ECB (fail = `{status, failed_lines}`) |
| OCP · YAML · GUI (세션 3 범위 밖) |

---

## 5. GREEN

| 규칙 |
|------|
| **1커밋 = 1 RED 묶음** · commit은 사용자 요청 시만 |
| **`src/constants.py`** — `METER_TO_FEET=3.28084` · `METER_TO_YARD=1.09361` · `DISPLAY_DECIMALS=1` |
| 이번 Test ID **최소**만 · 다른 ID 선행 GREEN 금지 |
| entity → boundary import 금지 |

---

## 6. REFACTOR

- 전제: `python -m pytest tests/ -v` **전부 PASS** (smell/safe)
- Budget: 파일≤3 · 클래스≤1 · 메서드≤3
- golden · assert 의미 **유지**

---

## 7. Track A vs B

| | **Logic (B)** | **UI (A)** |
|--|---------------|------------|
| API | `unit_convert(user_input)` | `UnitConverter.py` |
| 테스트 | `tests/test_unit_convert.py` | `tests/test_unit_converter.py` · `capsys` |
| Mock | Domain mock **금지** | stdout/input만 |

---

## 8. Command 체인

```
/red-test-plan → /red-skeleton → /tdd-red
→ /green-minimal → /golden-master
→ /refactor-smell → /refactor-safe
→ /export-session (/export)
```

Command 본문 > 본 Skill. 충돌 시 **tests golden** 우선.

---

## 9. API · golden (`.cursorrules`)

```python
unit_convert(user_input: float) -> {
    "status": "pass" | "fail" | "incomplete",
    "failed_lines": [...],
}
```

| Test ID | 입력 | Then |
|---------|------|------|
| **T1** | `-1` | `fail` · `negative_input` |
| **T2** | `2.5` | pass 3줄: `2.5 meter = 2.5 meter` · `= 8.2 feet` · `= 2.7 yard` |
| **T3** | `1` | pass: `1.0 meter` · `3.3 feet` · `1.1 yard` |

**CLI 오류 (boundary):**

| 입력 | stdout |
|------|--------|
| `meter2.5` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| `cubit:1` | `Unknown unit: cubit` |

표시 1자리 Rule ③ · 정밀 TC(8.2021, 0.9144) **분리** Rule ⑤.

---

## 10. pytest

```bash
python -m pytest tests/ -v
python -m pytest tests/test_unit_convert.py::test_t1_negative_input_fail -v
python -m pytest tests/ -v -k "t1 or meter25"
```

Golden: `UPDATE_GOLDEN=1 pytest …::test_*_golden -v` (PowerShell: `$env:UPDATE_GOLDEN="1"`)

---

## 11. entity 보조 (실습 확장)

프로젝트 `src/entity/` — Magic Square lab · ARRR Command와 **별도 RED 묶음**.

| 상수 | 값 |
|------|-----|
| `GRID_SIZE` | 16 |
| `MAGIC_SUM` | 34 |

`tests/conftest.py` · `grid_g1` — entity TC 전용.

---

## 12. 보고 형식

Command별 템플릿은 각 `.cursor/commands/*.md` **보고 형식** 따름.  
Export: **unit_converter-DOC** Skill · `/export-session`.

---

## Agent 체크list

- [ ] Phase 첫 줄
- [ ] RED: tests/만 · 의도 FAILED
- [ ] GREEN: constants · 1묶음 · PASS
- [ ] REFACTOR: Budget · golden 유지
- [ ] 한국어 · 최소 diff · git commit 임의 금지
