---
name: unit_converter-doc
description: >-
  Session Report and Transcript Export for UnitConverter_27.
  Use for Report Export, Transcript, /export-session, /export, Phase repeat,
  ARRR 1-cycle completion reports, or session N report requests (세션 N 보고서).
disable-model-invocation: true
---

# UnitConverter DOC — Report · Transcript Export

세션 산출물 **Report/** + **Prompting/** `NN.*` 쌍 Export.

**SSOT:** [Report/05.REPORT.md](../../Report/05.REPORT.md) · [Prompting/05.Export-Transcript.md](../../Prompting/05.Export-Transcript.md) · [export-session.md](../../commands/export-session.md) · `.cursorrules`

**Export 요청 시 unit_converter-DOC Skill 로드 후 [phase-checklist.md](phase-checklist.md) 수행.**

`/export-session` · `/export` 단독 입력 → 자동 추출 · **확인 질문 금지**

---

## Phase 선언

```
Phase: EXPORT
```

`Phase: repeat` — ARRR 1사이클 완료 Report (STEP: repeat)

---

## Step A → F

| Step | 작업 |
|------|------|
| **A** | `git status --short` · `python -m pytest tests/ -v` · Phase · Test ID · Command · uuid |
| **B** | `NN = max(Report/NN.*, Prompting/NN.*) + 1` |
| **C** | [report-template.md](report-template.md) → `Report/NN.REPORT.md` |
| **D** | [transcript-template.md](transcript-template.md) → `Prompting/NN.Export-Transcript.md` |
| **E** | README **Session Reports** 1행 |
| **F** | 경로 2개 · pytest 실측 보고 |

---

## 파일명

| | 경로 |
|--|------|
| Report | `Report/NN.REPORT.md` |
| Transcript (05 SSOT) | `Prompting/NN.Export-Transcript.md` |
| `/export` 변형 | `NN.Transcript.md` (동일 NN) |

---

## Report 목차

1. 메타 · 2. 요약 · 3. Phase STEP 또는 산출물 · 4. 계약·Rule · 5. 구현 · 6. pytest(**실측**) · 7. 다음

워크북 `Report/STEP3_*` **복붙 금지** — 링크만.

---

## Transcript

- `_Exported on {date} from Cursor_`
- `_Source: {uuid}.jsonl_`
- **User (Turn N)** / **Cursor (Turn N)**
- 생성 파일 표 · 마지막 줄 고지

---

## 금지

| 금지 |
|------|
| `src/` · `tests/` · `.cursorrules` 내용 변경 (Export만) |
| 채팅·터미널 **없는** pytest |
| `git commit` · `UPDATE_GOLDEN` 임의 |
| Report 또는 Transcript **단독** |

---

## 완료 보고

```markdown
Phase: EXPORT

## 생성 파일
- Report/NN.REPORT.md
- Prompting/NN.Export-Transcript.md

## 순번
- NN = {NN}

## pytest (Step A 실측)
- …

## README
- Session Reports NN 행 추가

## 다음
- (한 줄)
```

---

## 참고

| 파일 | 용도 |
|------|------|
| [report-template.md](report-template.md) | Report 골격 |
| [transcript-template.md](transcript-template.md) | Transcript 골격 |
| [phase-checklist.md](phase-checklist.md) | A~F 체크 |
| [unit_converter-tdd/SKILL.md](../unit_converter-tdd/SKILL.md) | TDD · Command |

Mom Test: `Report/STEP1_*`~`STEP3_*` · `Prompt/` = Export **아님**
