# Export — Report + Transcript

> **`/export-session` 별칭.** SSOT·절차는 [export-session.md](export-session.md) 따름.

UnitConverter_27 세션 산출물을 **번호 접두 `NN.XXX`** 형식으로 내보낸다.
---

## Phase 선언 (필수)

응답 **첫 줄**:

```
Phase: EXPORT
```

---

## 저장 규칙

| 항목 | 경로 | 파일명 |
|------|------|--------|
| **보고서** | `Report/` | `NN.REPORT.md` |
| **Transcript** | `Prompting/` | `NN.Transcript.md` |

- `NN` = **2자리 순번** (`01`, `02`, …). `Report/`·`Prompting/` 각각 **독립** 최대값+1. (보통 **같은 NN** 쌍으로 저장)
- `XXX` = 고정 접미: `REPORT` · `Transcript`
- 기존 `STEP*.md`·`Prompt/` 파일은 **덮어쓰지 않음**

### 순번 결정

```
Report/     → 01.REPORT.md, 02.REPORT.md … 중 최대 NN + 1
Prompting/  → 01.Transcript.md … 중 최대 NN + 1
```

첫 Export: **`01.REPORT.md`** + **`01.Transcript.md`**

---

## Report (`NN.REPORT.md`) 목차

1. **메타** — Export 일시 · 세션 · NN
2. **요약** — 이번 세션 한 문장
3. **산출물** — 생성·수정 파일 표
4. **계약·Rule** — `.cursorrules` 핵심 (SSOT, API, golden 요약)
5. **구현 상태** — 파일별 RED/GREEN/스텁
6. **테스트 상태** — pytest collect/run 결과
7. **다음 단계** — TDD Phase · 미완 TC

Mom Test 워크북(`Report/STEP3_*.md`) 내용 **복붙 금지** — 요약·링크만.

---

## Transcript (`NN.Transcript.md`) 규칙

- **출처:** Cursor `agent-transcripts/**/*.jsonl` (현재 프로젝트)
- **형식:** Markdown · `### USER` / `### ASSISTANT` 턴 구분
- **포함:** 사용자 `<user_query>` 본문 · assistant **최종 답변** 텍스트
- **제외:** tool call 상세 · `[REDACTED]` · thinking
- **최근 세션 우선** — 필요 시 이전 transcript 1개까지 병합

---

## Export 절차

1. `Report/`·`Prompting/`에서 다음 `NN` 확인
2. 프로젝트 상태 수집 (`.cursorrules`, `src/`, `tests/`, `pytest`)
3. `Report/NN.REPORT.md` 작성
4. agent-transcripts → `Prompting/NN.Transcript.md` 변환
5. **보고 형식**으로 경로·NN 출력

---

## 보고 형식 (Export 완료 시)

```markdown
Phase: EXPORT

## 생성 파일
- Report/NN.REPORT.md
- Prompting/NN.Transcript.md

## 순번
- NN = 01 (예)

## pytest (있으면)
- ...

## 다음
- (한 줄)
```

---

## 금지

- `src/` · `tests/` · `.cursorrules` **내용 변경** (Export는 **문서 생성만**)
- `STEP*.md` 삭제·이름 변경
- Transcript 원본 jsonl 수정
- 순번 **건너뛰기**·임의 파일명

---

## 참고

- Mom Test: `Report/STEP1_*` ~ `STEP3_*`
- 프롬프트 아카이브: `Prompt/` (Export 대상 **아님** — `Prompting/` = Transcript 전용)
