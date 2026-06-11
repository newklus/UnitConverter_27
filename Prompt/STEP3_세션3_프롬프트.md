# STEP 3 — Mom Test 결과 & 세션 3 워크북 프롬프트 (UnitConverter_27)

## 1. STEP 3 실행 프롬프트 (초기)

```
UnitConverter_27 STEP 3 Mom Test 결과:
- 페르소나: [...]
- 진짜 문제 (한 문장): [...]
- Mom Test 증거 3줄: [...]
UnitConverter_27 세션 3 워크북을 채워줘:
1) 주제 한 문장 (Mom Test 기반, 솔루션 최소화)
2) R-G-I-O (Role/Goal/Input/Output)
3) 성공 기준 3개 (Mom Test 증거와 연결)
4) 표면 문제 — 이번 프로젝트에서 하지 않을 것
8계층 중 이번 세션에서 만드는 것만: Rule, Command, (Skill), Test Loop
```

---

## 2. STEP 3 보강 프롬프트 (추궁 + README 자릿수)

```
고칠 질문에 대해 대답해줘
```

**추궁 질문**

```
README `1 meter = 1.09361 yard`와 교재 `1 yard = 0.9144 m`가 동시에 보였을 때,
그날 처음 돌려본 입력이 meter:1이었나요 yard:1이었나요—
그 한 번 실행에서 화면에 찍힌 숫자가 뭐였나요?
```

```
방금 내용까지 적용해서 UnitConverter_27 STEP 3 Mom Test 결과 업데이트해줘
```

```
readme에 정의된 자리수에대한 충돌이 있는것 같은데?
```

```
해줘
```

→ **Rule 1문단**: 내부 5자리(상수) · 출력 1자리(예시) · TC 표시/정밀 분리

---

## 3. 전제 (STEP 1·2 산출물 활용)

| 단계 | 산출물 | 세션 3에서 쓰는 방식 |
|------|--------|----------------------|
| STEP 1 | DIY 쇼핑 사용자 Mom Test | **표면 문제·하지 않을 것** |
| STEP 2 | 과제 학생 3턴 시뮬 | **페르소나·진짜 문제·증거** (주) |
| STEP 2 추궁 | `meter:1` → `yard:1` 순서·출력 | **증거 ②·Rule·성공 기준** |
| README 분석 | 예시 1자리 vs 상수 5자리 vs 「정확히」 | **Rule 1문단·표면 문제** |
| STEP 3 | 세션 3 워크북 | **Rule/Command/Skill/Test Loop** |

---

## 4. README 자릿수 Rule (워크북에 넣을 1문단)

```
내부 계산은 README 상수 풀 정밀도,
화면 출력은 README 예시와 동일 소수 1자리 반올림,
pytest는 표시값 TC와 내부 정밀도 TC를 구분해 명시한다.
```

| 입력 | 출력 (1자리) | README 근거 |
|------|--------------|-------------|
| `meter:2.5` | 8.2 ft, 2.7 yd | 기본 요구사항 예시 |
| `meter:1` | 3.3 ft, 1.1 yd | 예시 스타일 extrapolation |
| `yard:1` | 0.9 m (표시), 0.9144 m (정밀 TC) | 교재 역관계 |

---

## 5. 워크북 섹션별 작성 가이드

### Mom Test 증거 ② (업데이트)

- `meter:1` **먼저** → 1.09361 yard
- `yard:1` **다음** → 0.9144 m
- README **1자리 예시** vs 코드 **5자리** → 0.01 혼란

### Rule 계층 (필수)

- meter 기준 · README 상수
- **출력 1자리** (README 예시)
- **TC 표시/정밀 분리**
- 검증 순서 `meter:1` → `yard:1`

### 표면 문제 추가

- float 그대로 출력 = README 예시와 충돌
- 「정확히」= 표시 5자리만 = README 예시와 충돌

---

## 6. Report 저장

**저장 위치**

- `Report/STEP3_세션3_워크북.md`
- `Prompt/STEP3_세션3_프롬프트.md`
