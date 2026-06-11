# Refactor Safe — ARRR R단계 (Refine ⑧)

**/refactor-smell** 후보 **1개** — Change Budget 내 **안전 리팩터** + pytest 회귀 확인.

**unit_converter-tdd** Skill이 있으면 **자동 따름**.

SSOT: `tests/` golden **>** `docs/PRD.md` **>** `.cursorrules` **>** `README.md` · golden `tests/golden/*.approved.txt`

---

## Phase 선언 (필수)

응답 **첫 두 줄**:

```
Phase: refactor
Scope: src/ tests/
Track: Logic+UI
```

| 필드 | 값 |
|------|-----|
| **Phase** | `refactor` — Refine ⑧ (Budget 내 **수정** 허용) |
| **Scope** | `src/` · `tests/` (구조만 · assert/golden 의미 **불변**) |
| **Track** | `Logic+UI` |

**한 번에 refactor-safe만.** smell 재탐지 · GREEN · assert 완화 금지.

---

## 단독 입력 (필수)

`/refactor-safe` **만** 입력 시 **직전 refactor-smell·채팅**에서 추출. **확인 질문 금지.**

| 추출 | 출처 |
|------|------|
| **스멜·P** | smell 표 · 후보 #1 (없으면 Duplicated Code·Magic Number 휴리스틱) |
| **대상 파일** | smell 후보 · `src/entity/` · `src/unit_convert.py` |
| **Budget** | smell 표 — 기본 **파일≤3 · 클래스≤1 · 메서드≤3** |
| **Test ID** | 관련 TC · entity / UnitConverter |

---

## 전제

```bash
python -m pytest tests/ -v
```

| 결과 | 동작 |
|------|------|
| **전부 PASSED** | 리팩터 **진행** |
| **FAILED** | **중단** — GREEN/fix 먼저 (entity-only refactor 시 entity TC PASS 확인) |

---

## Change Budget (1회 상한)

| 항목 | ≤ |
|------|---|
| **파일** | 3 |
| **클래스** | 1 |
| **메서드** | 3 |

- Budget **초과** → 작업 **분할** · 이번 턴은 extract 1~2메서드만
- **golden** · approval assert **의미 변경 금지**

---

## 절차 (순서 고정)

| # | 단계 | 작업 |
|---|------|------|
| 1 | **pytest PASS** | 전체 또는 영향 범위 — 실패 시 중단 |
| 2 | **extract / 이동** | Budget 내 · `constants.py` SSOT 유지 |
| 3 | **ECB** | entity→boundary import **추가 금지** |
| 4 | **pytest 회귀** | `python -m pytest tests/ -v` |
| 5 | **보고** | Extract · Budget · 변경 파일 · 회귀 |

---

## 허용 · 금지

| 허용 | 금지 |
|------|------|
| extract method · import 정리 · 중복 제거 | assert 완화 · skip · xfail |
| `entity/validation.py` 등 **구조** 파일 추가 | 동작·golden·API 계약 변경 |
| tests **import 경로**만 수정 | `.approved.txt` 수동 편집 |
| | E001~E005 emit · ECB 신규 |
| | Budget 초과 · 다중 smell 동시 해결 |
| | **git commit** (사용자 요청 시만) |

---

## 예시 (UnitConverter_27 · entity)

| 스멜 | Extract | Budget |
|------|---------|--------|
| Duplicated Code — 10선 합 4곳 | `sum_line` · `magic_line_indices` → `validation.py` | 2파일 / 2메서드 |
| Magic Number | `METER_TO_FEET` → `src/constants.py` | 2파일 / 0클래스 |

```python
# validation.py — extract SSOT
def sum_line(grid, indices): ...
def magic_line_indices(): ...  # 4행+4열+2대각=10선
```

---

## pytest

```bash
python -m pytest tests/ -v
python -m pytest tests/entity/ -v
```

**회귀 실패:** assert 완화 **금지** — 리팩터 롤백 또는 구현 수정 후 재실행.

---

## 보고 형식 (완료 시)

```markdown
Phase: refactor
Scope: src/ tests/
Track: Logic+UI

## Refactor Safe
| 스멜 | Extract | Budget |
|------|---------|--------|
| Duplicated Code | sum_line, magic_line_indices | 2파일/2메서드 |

## pytest
- `python -m pytest tests/ -v` → N passed (회귀 없음)

## 변경 파일
- src/entity/validation.py (신규)
- src/entity/solve.py

## golden
- 변경 없음 · matched 유지

## 다음
- `/refactor-smell` (다음 후보) 또는 `/export-session`
```

---

## Command 흐름

```
/red-test-plan → /red-skeleton → /tdd-red
/green-minimal → /golden-master
/refactor-smell → /refactor-safe (본 Command)
/export-session
```

---

## Skill 참조

> **unit_converter-tdd** — Budget · ECB · constants · 10선 `MAGIC_SUM=34`  
> **unit_converter-DOC** — ARRR 1사이클 완료 시 `/export-session`
