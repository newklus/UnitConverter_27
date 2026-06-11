# Export-session — Report + Transcript

UnitConverter_27 세션 산출물을 **번호 접두 `NN.XXX`** 쌍으로 내보낸다. `/export` **별칭**.

**unit_converter-DOC** Skill이 있으면 **자동 따름** — [phase-checklist.md](../skills/unit_converter-DOC/phase-checklist.md) Step A~F.

SSOT: `Report/05.REPORT.md` · `Prompting/05.Export-Transcript.md` **>** `.cursorrules` · `docs/PRD.md`(없으면 생략)

---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: EXPORT
```

---

## 단독 입력 (필수)

`/export-session` 또는 `/export` **만** 입력 시 **채팅 전체**에서 자동 추출. **확인 질문 금지.**

| 추출 | 출처 |
|------|------|
| 세션 주제 | 채팅 핵심 작업 |
| Phase · Test ID · Command | 채팅·`.cursor/commands/` |
| 산출물 | 생성·수정 파일 |
| Transcript | `agent-transcripts/**/*.jsonl` |

---

## 저장 규칙

| 항목 | 경로 | 파일명 (05 SSOT) |
|------|------|------------------|
| **보고서** | `Report/` | `NN.REPORT.md` |
| **Transcript** | `Prompting/` | `NN.Export-Transcript.md` |

- `NN` = `max(Report/NN.*, Prompting/NN.*) + 1` (2자리)
- `/export` Command 변형: `NN.Transcript.md` 허용 — **동일 NN** 쌍
- `STEP*.md` · `Prompt/` **덮어쓰기 금지**

---

## 절차 (unit_converter-DOC 연동)

Export 요청 시 **unit_converter-DOC Skill 로드 후 checklist 수행.**

| Step | 작업 |
|------|------|
| **A** | `git status` · `python -m pytest tests/ -v` · Phase · Test ID · Command |
| **B** | NN 결정 |
| **C** | [report-template.md](../skills/unit_converter-DOC/report-template.md) → Report |
| **D** | [transcript-template.md](../skills/unit_converter-DOC/transcript-template.md) → Transcript |
| **E** | README **Session Reports** 표 1행 추가 |
| **F** | 완료 보고 (경로 2개) |

---

## Report (`NN.REPORT.md`)

1. **메타** — 프로젝트 · 단계 · 일시 · NN · 목적
2. **요약** — 한 문장
3. **핵심 결정·산출물** (또는 Phase별 STEP: RED/GREEN/REFACTOR/repeat)
4. **계약·Rule** — `.cursorrules` 요약 (워크북 **복붙 금지**)
5. **구현 상태** · **pytest** (Step A **실측**만)
6. **다음 단계**

**마지막 줄:** `*본 문서는 Report/NN.REPORT.md — {주제}입니다.*`

---

## Transcript (`NN.Export-Transcript.md`)

- `_Exported on {YYYY-MM-DD} from Cursor_`
- `_Source: {uuid}.jsonl_`
- **User (Turn N)** / **Cursor (Turn N)** — tool·thinking 제외
- 생성·수정 파일 표
- **마지막 줄:** `*본 문서는 Prompting/NN.Export-Transcript.md — …입니다.*`

---

## 보고 형식 (완료 시)

```markdown
Phase: EXPORT

## 생성 파일
- Report/NN.REPORT.md
- Prompting/NN.Export-Transcript.md

## 순번
- NN = {NN}

## pytest (Step A 실측)
- …

## 다음
- (한 줄)
```

---

## 금지

| 금지 | |
|------|--|
| `src/` · `tests/` · `.cursorrules` **내용 변경** | Export = 문서만 |
| **채팅·터미널에 없는 pytest** | Step A 미실행 시 기재 금지 |
| `git commit` · `UPDATE_GOLDEN` **임의** | |
| Transcript jsonl 수정 · NN 건너뛰기 | |
| Report **또는** Transcript **단독** | 쌍 필수 |

---

## 참고

- Mom Test: `Report/STEP1_*` ~ `STEP3_*`
- ARRR Command: `.cursor/commands/red-test-plan.md` ~ `refactor-safe.md`
- TDD Skill: `.cursor/skills/unit_converter-tdd/SKILL.md`
