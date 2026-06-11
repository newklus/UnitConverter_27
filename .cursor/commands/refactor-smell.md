# Refactor Smell — ARRR R단계 (Refine ⑦)

**코드 스멜 탐지만** — 분석·표·후보 제안. **수정·commit 금지.**

**unit_converter-tdd** Skill이 있으면 **자동 따름** (계층·네이밍·ECB 규칙).

SSOT: `tests/` golden **>** `docs/PRD.md` **>** `.cursorrules` **>** `README.md` · 상수 **`constants.py`**

**Skill:** `unit_converter-tdd` — ECB · constants · 스멜 가중치.

---

## Phase 선언 (필수)

응답 **첫 두 줄**:

```
Phase: refactor
Scope: src/ tests/
Track: Logic+UI
```

| 필드 | 값 | 비고 |
|------|-----|------|
| **Phase** | `refactor` | ARRR R = Refine ⑦ (스멜 **탐지**만) |
| **Scope** | `src/` · `tests/` | 분석 대상 · **수정 금지** |
| **Track** | `Logic+UI` | entity · boundary · CLI 동시 점검 |

**한 번에 refactor-smell만.** 코드 diff · `/refactor-safe` 실행 · commit **금지**.

---

## 역할 · 범위

| 항목 | 내용 |
|------|------|
| **선행** | GREEN·Golden Master 완료 권장 · **전체 pytest PASS** |
| **산출물** | 스멜 표(P0/P1/P2) · Change Budget · `/refactor-safe` 후보 1~3개 |
| **목적** | 리팩터 **전** 냄새·우선순위·예산 가시화 |
| **다음 단계** | **P0 1개** 선택 → `/refactor-safe` |

---

## 전제 (중단 조건)

```bash
python -m pytest tests/ -v
```

| 결과 | 동작 |
|------|------|
| **전부 PASSED** | 스멜 탐지 **진행** |
| **1개라도 FAILED** | **즉시 중단** — 스멜 표 출력 **금지** · GREEN/fix 먼저 |

- RED·스텁·golden mismatch 상태에서 refactor-smell **실행하지 않음**.

---

## 자동 추출 (추가 입력 없음)

`/refactor-smell` **단독** 입력 시 **프로젝트·채팅**에서 추출. **확인 질문 금지.**

| 추출 항목 | 출처 |
|-----------|------|
| **분석 범위** | `src/` · `tests/` · `UnitConverter.py` (boundary) |
| **계층** | entity / boundary · import 그래프 |
| **상수·매직넘버** | `constants.py` vs 리터럴 반복 |
| **최근 GREEN** | green-minimal · golden-master 산출 |

---

## 스멜 유형 · 우선순위

| 우선순위 | 스멜 | 탐지 기준 (휴리스틱) |
|----------|------|----------------------|
| **P0** | **ECB 위반** | entity→boundary/control import · E001~E005 emit · 계층 역전 |
| **P0** | **Magic Number** | `constants.py` 밖 반복 리터럴 (3.28084, 1.09361 등) |
| **P1** | **Duplicated Code** | 동일 로직·포맷 문자열 2곳+ (`round`·3줄 포맷 등) |
| **P1** | **Feature Envy** | 함수가 다른 모듈 데이터·상수만 다루며 자기 책임 없음 |
| **P1** | **Mysterious Name** | `a`, `tmp`, `x` 등 의미 불명 식별자 (meter/feet/yard 도메인 용어 불일치) |
| **P2** | **Long Method** | 본문 **>25줄** 또는 분기·책임 3개+ (테스트 Arrange+Act+Assert 혼재) |

### ECB · 프로젝트 특화 (P0)

| 위반 | 예 |
|------|-----|
| src → boundary 역전 | `unit_convert.py`가 `UnitConverter` import |
| src → CLI | I/O·`input()`·`capsys` in `src/unit_convert.py` |
| E001~E005 | `raise E001` · `return "E002"` — dict/문자열 계약 위반 |
| golden 우회 | `.approved.txt` 수동 편집 흔적 (탐지 시 보고만) |

### Magic Number (P0/P1)

| 위치 | SSOT |
|------|------|
| `src/unit_convert.py` | `src/constants.py` |
| tests | golden **literal 허용** · production 복붙은 P1 |

---

## Change Budget (refactor-safe 예산)

`/refactor-safe` 1회 실행 시 **권장 상한** — smell 탐지 단계에서 **예산 초과 후보 표시**.

| 항목 | 상한 |
|------|------|
| **파일** | ≤ 3 |
| **클래스** | ≤ 1 |
| **메서드** | ≤ 3 |

- 후보 제안 시 **예상 diff**가 Budget 초과 → P2로 강등 또는 **분할** 제안 (수정은 refactor-safe에서).

---

## 절차 (순서 고정)

| # | 단계 | 작업 |
|---|------|------|
| 1 | **pytest PASS** | `python -m pytest tests/ -v` — 실패 시 **중단** |
| 2 | **범위 스캔** | `src/` · `tests/` · `UnitConverter.py` (Track UI) |
| 3 | **스멜 분류** | P0/P1/P2 · 유형별 표 작성 |
| 4 | **Budget 점검** | 후보별 파일·클래스·메서드 수 추정 |
| 5 | **후보 1~3개** | `/refactor-safe` 넘길 항목 (P0 우선) |
| 6 | **보고** | 표 + 다음 안내 — **코드 수정 없음** |

---

## 출력 형식 (필수)

```markdown
Phase: refactor
Scope: src/ tests/
Track: Logic+UI

## pytest
- `python -m pytest tests/ -v` → N passed (전부 PASS — 진행)

## 스멜 표
| P | 유형 | 위치 | 요약 | Budget (파일/클래스/메서드) |
|---|------|------|------|---------------------------|
| P0 | Magic Number | src/unit_convert.py | (스텁 — GREEN 후 재점검) | — |
| P1 | Duplicated Code | tests/test_unit_convert.py | 3줄 golden assert 패턴 | 1/0/0 |

## /refactor-safe 후보 (1~3)
| # | P | 대상 | 리팩터 의도 | Budget |
|---|---|------|-------------|--------|
| 1 | P0 | src/constants.py + unit_convert | METER_TO_* SSOT 추출 | 2/0/2 |
| 2 | P1 | unit_convert | 3줄 포맷 헬퍼 공통화 | 2/0/1 |

## 다음
- **P0 후보 1개**만 골라 `/refactor-safe` 실행
- pytest 전부 PASS 유지 확인 후 진행
```

**pytest FAILED 시 출력:**

```markdown
Phase: refactor
Scope: src/ tests/
Track: Logic+UI

## pytest — 중단
- `python -m pytest tests/ -v` → X failed
- refactor-smell **중단** — GREEN/fix 후 재실행

## 다음
- 실패 TC GREEN · `/green-minimal`
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` · `tests/` · `UnitConverter.py` 수정** | Refine ⑦ = 탐지만 |
| **`git commit` / `push`** | refactor-safe·사용자 요청까지 |
| assert 완화 · golden 수동 편집 | SSOT 훼손 |
| `/refactor-safe` **동시 실행** | smell → safe 2단계 |
| Budget 무시 대규모 리팩터 제안 | 1회 safe = 작은 diff |

---

## Command 흐름 (ARRR 실습)

```
/red-test-plan → … → /golden-master → /refactor-smell (본 Command)
→ /refactor-safe → /export-session
```

---

## UnitConverter_27 참고

| 영역 | 흔한 스멜 |
|------|-----------|
| `unit_convert.py` | 스텁 · Magic Number( GREEN 후 ) · Long Method(3줄 포맷) |
| `tests/` | golden assert 중복 · approval 포맷 문자열 분산 |
| `UnitConverter.py` | boundary Feature Envy(entity 미호출) · CLI golden 분리 |

- **현재 T1 FAILED** → refactor-smell **중단** (전부 PASS 전제).

---

## Skill 참조

> **unit_converter-tdd** Skill이 있으면 **자동 따름** — ECB·row-major·constants·Test ID 네이밍 기준으로 스멜 가중치.

Skill 없음 → 본 Command + `.cursorrules` + import/static 휴리스틱.

---

## 보고 마지막 줄 (필수)

```
P0 후보 1개를 골라 /refactor-safe 를 실행하세요.
```
