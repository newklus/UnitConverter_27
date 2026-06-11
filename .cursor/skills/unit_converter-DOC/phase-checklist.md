# Phase Checklist — Export · ARRR 1사이클

`/export-session` · `/export` · `Phase: repeat` · **unit_converter-DOC**

---

## Step A — 입력 수집 (실행 필수)

| # | 항목 | 명령 |
|---|------|------|
| A1 | git | `git status --short` |
| A2 | pytest | `python -m pytest tests/ -v` (**실측**) |
| A3 | Phase | red / green / refactor / repeat / EXPORT |
| A4 | Track | Logic (`unit_convert`) / UI (`UnitConverter.py`) |
| A5 | Test ID | T1, T2, U-IN-01, … |
| A6 | Command | /red-test-plan, /export, … |
| A7 | uuid | agent-transcripts 최신 jsonl |

**금지:** A2 없이 pytest 결과 기재

---

## Step B — NN

```
NN = max(Report/NN.*, Prompting/NN.*) + 1
```

- [ ] 덮어쓰기 없음 · STEP*.md 유지

---

## Step C — Report

- [ ] `Report/NN.REPORT.md`
- [ ] [report-template.md](report-template.md)
- [ ] Phase STEP · Transcript 링크 · pytest 실측

---

## Step D — Transcript

- [ ] `Prompting/NN.Export-Transcript.md`
- [ ] [transcript-template.md](transcript-template.md)
- [ ] `_Exported on` · `_Source uuid`

---

## Step E — README

```markdown
## Session Reports
| NN | 주제 | Report | Transcript |
| NN | … | [Report/NN.REPORT.md](Report/NN.REPORT.md) | [Prompting/NN.Export-Transcript.md](Prompting/NN.Export-Transcript.md) |
```

---

## Step F — 보고

Phase: EXPORT · 경로 2개 · NN · pytest 실측 · README

---

## ARRR repeat

| Phase | 증거 |
|-------|------|
| RED | tests/ · FAILED 의도 |
| GREEN | src/ · PASS |
| REFACTOR | Budget · golden |

---

## 금지

- git commit / UPDATE_GOLDEN 임의
- src/tests/.cursorrules Export 외 변경
- Report·Transcript 단독
- pytest 추측
