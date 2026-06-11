# RED Test Plan — ARRR A단계 (Ask = RED ③)

**C2C 설계표 + 테스트 플랜만** 작성한다. 코드·테스트 파일은 **생성하지 않는다**.

SSOT: `docs/PRD.md` **>** `.cursorrules` **>** `README.md` · `Report/STEP3_세션3_워크북.md`  
(`docs/PRD.md` 없으면 `.cursorrules` Rule·API·golden을 FR로 매핑)

**Skill:** `unit_converter-tdd` — 명시 호출·본 Command 시 자동 참조.

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
| **Phase** | `red` | ARRR A = RED ③ (설계·플랜만) |
| **Layer** | `entity` \| `boundary` | Logic Track 기본 = `entity` |
| **Track** | `Logic` \| `UI` | Domain 로직 = `Logic` |

**Track A (boundary):** 본 Command 그대로 — **`Layer: boundary`** 만 바꾸면 재사용. Track·출력 4블록·금지 동일.

---

## 자동 추출 (추가 입력 없음)

`/red-test-plan` **단독** 입력 시 아래를 **채팅·PRD·SSOT**에서 추출. **확인 질문 금지.**

| 추출 항목 | 출처 |
|-----------|------|
| **세션 주제** | 현재 채팅 핵심 작업 (예: T1 음수 fail RED) |
| **Test ID** | 채팅·PRD·기존 TC (예: `T1`, `T2`) — 없으면 `T{n}` 순번 부여 |
| **대상 함수/API** | `.cursorrules` · PRD FR (예: `unit_convert`) |
| **FR 인용** | `docs/PRD.md` FR-* · 없으면 Rule ①~⑧·API 계약 |
| **RED 묶음** | 이번 플랜에 포함할 Test ID 집합 |

---

## 역할 · 범위

| 항목 | 내용 |
|------|------|
| **ARRR 단계** | **A (Ask)** = RED ③ — *무엇을 검증할지* 설계 |
| **산출물** | C2C 표 · Track B 표 · 테스트 플랜 · ECB·Mock 점검 (**문서만**) |
| **다음 단계** | `/red-skeleton` — 테스트 골격(함수 시그니처·import) 작성 |

**한 번에 red-test-plan만.** GREEN · REFACTOR · skeleton · pytest 본문 작성 금지.

---

## 출력 4블록 (필수 · 표 형식)

응답 본문은 **아래 4섹션 순서** 고정. 각 섹션 **표 필수**.

### 블록 1 — C2C (Rule1~3)

| Rule | 열 | 내용 |
|------|-----|------|
| **Rule1** | PRD FR | FR-ID + 인용 한 줄 (PRD 없으면 `.cursorrules` Rule/API) |
| **Rule2** | To-Do | **1개** — 이번 RED에서 검증할 행동 (동사로) |
| **Rule3** | Test ID · G/W/T | Test ID · **Given** · **When** · **Then** |

**예시 (UnitConverter_27 · Logic · entity):**

| PRD FR (Rule1) | To-Do (Rule2) | Test ID | Given | When | Then |
|----------------|---------------|---------|-------|------|------|
| FR-NEG (Rule ② · API fail) | 음수 meter 입력 시 fail dict 반환 검증 | **T1** | `user_input = -1` | `unit_convert(-1)` 호출 | `status=="fail"`, `failed_lines`에 `negative_input` |

---

### 블록 2 — Track B 표 (Logic Track)

| Test ID | 대상 함수 | Given → Then | Invariant | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| T1 | `unit_convert` | `-1` → fail + `negative_input` | `src/` 미구현·스텁 | `TypeError` 또는 `status` 불일치 assertion **FAILED** |
| T2 | `unit_convert` | `2.5` → pass 3줄 golden | 표시 1자리 Rule ③ | `incomplete` 또는 줄 불일치 **FAILED** |

- **Invariant:** RED 전까지 깨지면 안 되는 계약 (SSOT·Rule).
- **Expected RED Failure:** 스텁/미구현 시 pytest에 **드러날** 실패 유형.

---

### 블록 3 — 테스트 플랜

| 항목 | 값 (플랜 · 파일 생성 아님) |
|------|---------------------------|
| **파일 경로** | `tests/test_unit_convert.py` (Logic) · `tests/test_unit_converter.py` (CLI, 예정) |
| **함수명** | `test_t1_negative_input_fail`, `test_t2_meter_2_5_pass`, … |
| **conftest 픽스처** | (없음 — 순수 함수) · boundary Track 시 `capsys`/`tmp_path` 등 명시 |
| **pytest 명령** | `pytest tests/test_unit_convert.py -v` · `-k "t1 or t2"` |
| **RED 묶음 범위** | 이번 skeleton/red 본문에 넣을 Test ID 목록 (예: `T1`만 / `T1,T2`) |

---

### 블록 4 — ECB · Mock 점검

| Track | Layer | 점검 | 판정 |
|-------|-------|------|------|
| **Logic** | entity | Domain Mock 사용 | **금지** — `unit_convert` 순수 계산, mock/fake domain 없음 |
| **Logic** | entity | E001~E005 emit | **금지** — RED ③에서 ECB 이벤트·에러 emit 설계·코드 없음 |
| **Logic** | entity | 외부 I/O mock | **금지** — 파일·네트워크·CLI subprocess mock 불필요 |
| **UI** | boundary | (해당 시) render/capsys만 | Domain 로직 mock 금지 유지 |

**E001~E005:** RED ③ 플랜 단계에서 **에러 코드 emit·ECB 핸들러·이벤트 버스** 언급·설계·스텁 **금지**. fail은 `{status, failed_lines}` dict 계약으로만 기술.

---

## 금지

| 금지 | 이유 |
|------|------|
| `src/` · `UnitConverter.py` 수정 | GREEN Phase |
| GREEN · REFACTOR | red-test-plan = A(Ask) only |
| `tests/` · `src/` **파일 생성·수정** | `/red-skeleton` · `/tdd-red` 담당 |
| `@pytest.mark.skip` · `xfail` | RED 설계에 포함 금지 |
| assert 완화·기대값 낮추기 | SSOT 훼손 |
| Domain Mock (Logic Track) | 순수 함수·단위 테스트 |
| E001~E005 emit 설계 | ECB는 이후 Phase |
| OCP · YAML · GUI | `.cursorrules` 세션 3 범위 밖 |

---

## 보고 형식 (완료 시)

```markdown
Phase: red
Layer: entity
Track: Logic

## 1. C2C (Rule1~3)
| PRD FR | To-Do | Test ID | Given | When | Then |
| ... |

## 2. Track B
| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
| ... |

## 3. 테스트 플랜
| 파일 | 함수 | conftest | pytest | RED 묶음 |
| ... |

## 4. ECB · Mock 점검
| Track | Layer | 점검 | 판정 |
| ... |

/red-skeleton 으로 넘길 준비됐다
```

**마지막 줄 (필수, 한 줄):**

```
/red-skeleton 으로 넘길 준비됐다
```

---

## SSOT 매핑 (PRD 없을 때)

| PRD 대체 | `.cursorrules` / README |
|----------|-------------------------|
| FR-DISPLAY | Rule ③ · golden 1자리 · `meter:2.5` → 8.2/2.7 |
| FR-NEG | Rule ② · `user_input < 0` → fail |
| FR-API | `unit_convert(user_input: float) → {status, failed_lines}` |
| FR-CLI | `UnitConverter.py` · `단위:값` · 오류 메시지 SSOT |
| FR-PREC | Rule ⑤ · 정밀 TC 분리 (표시 TC와 혼합 금지) |

---

## Command 흐름 (ARRR 실습)

```
/red-test-plan    → C2C + Track B + 플랜 (본 Command)
/red-skeleton     → pytest.fail 골격
/tdd-red          → assert RED
/green-minimal    → 최소 GREEN
/golden-master    → Approval baseline
/refactor-smell   → 스멜 탐지
/refactor-safe    → Budget 리팩터
/export-session   → Report + Transcript (/export 별칭)
```

---

## 참고

- TDD Phase 표: `.cursorrules` — RED는 `tests/`만; **red-test-plan은 tests/도 건드리지 않음**
- 기존 TC: `tests/test_unit_convert.py` · `test_t1_negative_input_fail` (T1 RED 완료 시 skeleton/red에서 참조)
- Mom Test golden: `.cursorrules` 표시 golden 표
