# Report Template — NN.REPORT.md

SSOT: [Report/05.REPORT.md](../../Report/05.REPORT.md) · `.cursorrules`

---

```markdown
# UnitConverter_27 — {세션 주제}

| 항목 | 내용 |
|------|------|
| **프로젝트** | UnitConverter_27 — meter 기준 길이 단위 변환기 |
| **단계** | 세션 3 · {Phase: red \| green \| refactor \| repeat \| EXPORT} |
| **보고서 생성일** | YYYY-MM-DD |
| **순번** | **NN** |
| **목적** | {한 줄} |

**관련 Transcript:** [Prompting/NN.Export-Transcript.md](../Prompting/NN.Export-Transcript.md)

---

## 1. 요약

{한 문장}

---

## 2. {Phase STEP 또는 핵심 결정·산출물}

### STEP: RED

| Test ID | 함수 | 상태 | Command |
|---------|------|------|---------|
| T1 | test_t1_negative_input_fail | FAILED (의도) | /tdd-red |

### STEP: GREEN

| Test ID | 함수 | 상태 | Command |
|---------|------|------|---------|
| T2 | test_meter_2_5_pass | PASSED | /green-minimal |

### STEP: REFACTOR

| 스멜 | 대상 | Budget | Command |
|------|------|--------|---------|
| Magic Number | src/constants.py | 2파일/2메서드 | /refactor-safe |

### 산출물

| 구분 | 파일 |
|------|------|
| src/ | unit_convert.py · constants.py |
| tests/ | test_unit_convert.py |

---

## 3. 계약·Rule

- SSOT: tests/ > `.cursorrules` > README
- API: `unit_convert` → `{status, failed_lines}`
- 표시 1자리 · 정밀 TC 분리 (Rule ⑤)

[STEP3 워크북](STEP3_세션3_워크북.md) — 링크만.

---

## 4. 구현 상태

| 파일 | Phase |
|------|-------|
| src/unit_convert.py | RED/스텁 |
| UnitConverter.py | (boundary GREEN) |

---

## 5. 테스트 상태

`python -m pytest tests/ -v` — **Step A 실측** YYYY-MM-DD

| 결과 | 상세 |
|------|------|
| N passed, M failed | … |

---

## 6. 다음 단계

1. …

---

*본 문서는 Report/NN.REPORT.md — {주제} Export입니다.*
```

## Phase별 섹션

| Phase | 포함 STEP |
|-------|-----------|
| red | RED · pytest FAILED |
| green | GREEN · PASS |
| refactor | REFACTOR |
| repeat | RED→GREEN→REFACTOR 요약 |
| EXPORT | 산출물 · 번호 체계 (05형) |
