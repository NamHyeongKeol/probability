import random

def run_experiment(count):
  """
  세 개의 랜덤 실수를 뽑아 특정 조건에 따라 점수를 계산하는 실험을 수행합니다.

  Args:
    count: 실험 반복 횟수

  Returns:
    조건을 만족한 비율 (퍼센티지)
  """
  score = 0
  for _ in range(count):
    # 독립적으로 랜덤 실수 생성 (0.0 <= x < 1.0)
    a = random.random()
    b = random.random()
    c = random.random()

    # c와 a 비교 (복원된 로직)
    if c < a:
      # c가 a보다 작으면 b < a 인지 확인
      if b < a:
        score += 1
    else: # c >= a
      # c가 a보다 크거나 같으면 a < b 인지 확인
      if a < b:
        score += 1

  # 최종 비율 계산 및 출력
  if count == 0:
    return 0.0
  rate = (score / count) * 100
  return rate

# 실험 횟수 설정 (여기서 값을 변경할 수 있습니다)
num_trials = 1000000

# 실험 실행 및 결과 출력
result_rate = run_experiment(num_trials)
print(f"총 {num_trials}번의 시도 결과, 성공 비율은 {result_rate:.2f}% 입니다.")

# 간단한 분석: (복원된 분석)
# a, b, c는 [0, 1) 범위에서 독립적이고 균등하게 분포합니다.
# 점수를 얻는 조건은 (c < a 이고 b < a) 또는 (c >= a 이고 a < b) 입니다.
# 세 숫자 a, b, c의 모든 가능한 순서 배열(3! = 6가지)은 동일한 확률(1/6)을 가집니다.
# 1. a < b < c: c >= a 이고 a < b 이므로 점수 +1
# 2. a < c < b: c >= a 이고 a < b 이므로 점수 +1
# 3. b < a < c: c >= a 이고 a < b 가 아니므로 점수 +0
# 4. b < c < a: c < a 이고 b < a 이므로 점수 +1
# 5. c < a < b: c < a 이고 b < a 가 아니므로 점수 +0
# 6. c < b < a: c < a 이고 b < a 이므로 점수 +1
# 총 6가지 경우 중 4가지 경우에 점수를 얻으므로, 성공 확률은 4/6 = 2/3 입니다.
# 따라서 실험 결과는 약 66.67%에 가까운 값이 나올 것으로 예상됩니다.
