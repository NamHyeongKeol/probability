import random

def run_experiment(count):
  """
  여러 개의 랜덤 실수를 뽑아 특정 조건에 따라 점수를 계산하는 실험을 수행합니다.

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
    d = random.random()

    c_less_than_a = c < a
    d_less_than_a = d < a

    if c_less_than_a and d_less_than_a:
      # c, d 모두 a보다 작으면 b < a 인지 확인
      if b < a:
        score += 1
    elif c_less_than_a or d_less_than_a:
      # c, d 중 하나만 a보다 작으면 e를 뽑아 비교
      e = random.random()
      if e < a:
        # e가 a보다 작으면 b < a 인지 확인
        if b < a:
          score += 1
      else: # e >= a
        # e가 a보다 크거나 같으면 a < b 인지 확인
        if a < b:
          score += 1
    else: # c >= a and d >= a
      # c, d 모두 a보다 크거나 같으면 a < b 인지 확인
      if a < b:
        score += 1

  # 최종 비율 계산 및 출력
  if count == 0:
    return 0.0
  rate = (score / count) * 100
  return rate

# 실험 횟수 설정 (여기서 값을 변경할 수 있습니다)
num_trials = 100000 # 횟수를 늘려 정확도 확인

# 실험 실행 및 결과 출력
result_rate = run_experiment(num_trials)
print(f"총 {num_trials}번의 시도 결과, 성공 비율은 {result_rate:.2f}% 입니다.")

# 간단한 분석:
# a, b, c, d, e는 [0, 1) 범위에서 독립적이고 균등하게 분포합니다.
# 점수를 얻는 조건:
# 1. (c < a 이고 d < a) 이고 (b < a)
# 2. ((c < a 이고 d >= a) 또는 (c >= a 이고 d < a)) 이고 (e < a) 이고 (b < a)
# 3. (c >= a 이고 d >= a) 이고 (a < b)
# 각 변수가 a보다 작을 확률은 a의 값에 따라 달라지지만, 기댓값 측면에서 보면 각 비교는 1/2 확률입니다.
# P(c < a) ~ 1/2, P(d < a) ~ 1/2, P(e < a) ~ 1/2, P(b < a) ~ 1/2, P(a < b) ~ 1/2
# 각 케이스의 확률 근사치:
# Case 1: P(c<a) * P(d<a) * P(b<a) = (1/2) * (1/2) * (1/2) = 1/8
# Case 2: [P(c<a)*P(d>=a) + P(c>=a)*P(d<a)] * P(e<a) * P(b<a)
#         = [(1/2)*(1/2) + (1/2)*(1/2)] * (1/2) * (1/2)
#         = [1/4 + 1/4] * 1/4 = (1/2) * (1/4) = 1/8
# Case 3: P(c>=a) * P(d>=a) * P(a<b) = (1/2) * (1/2) * (1/2) = 1/8
# 전체 성공 확률 근사치 = 1/8 + 1/8 + 1/8 = 3/8 = 0.375 = 37.5%
# 따라서 실험 결과는 약 37.5%에 가까운 값이 나올 것으로 예상됩니다.
# (주의: 이는 각 변수가 a보다 작을 확률을 단순히 1/2로 가정한 근사치입니다. 실제로는 a값에 따라 달라지므로 약간의 오차가 있을 수 있습니다.) 