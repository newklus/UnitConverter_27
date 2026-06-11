# Transcript Template — NN.Export-Transcript.md

SSOT: [Prompting/05.Export-Transcript.md](../../Prompting/05.Export-Transcript.md)

---

```markdown
# UnitConverter_27 — Session Transcript

_Exported on {YYYY-MM-DD} from Cursor_

**관련 보고서:** [Report/NN.REPORT.md](../Report/NN.REPORT.md)

_Source: {uuid}.jsonl_

---

## User (Turn 1)

{user_query}

---

## Cursor (Turn 2)

{assistant 답변 — Phase·pytest·변경 파일}

---

## 생성·수정 파일

| 구분 | 파일 |
|------|------|
| src/ | … |
| tests/ | … |
| Report/ | Report/NN.REPORT.md |
| Prompting/ | Prompting/NN.Export-Transcript.md |

---

*본 문서는 Prompting/NN.Export-Transcript.md — {주제} Export입니다.*
```

## 규칙

| | |
|--|--|
| 턴 | User / Cursor (또는 ### USER / ### ASSISTANT) |
| 제외 | tool call · thinking · [REDACTED] |
| 출처 | `agent-transcripts/**/*.jsonl` |
| 품질 | 요약 Transcript 금지 · 생성 파일 표 필수 |

## 파일명

- **05 SSOT:** `NN.Export-Transcript.md`
- `/export` 변형: `NN.Transcript.md` — 동일 NN
