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

    if c < a:
      if b < a:
        score += 1
    else:
      if a < b:
        score += 1

  if count == 0:
    return 0.0
  rate = (score / count) * 100
  return rate

num_trials = 1000000

result_rate = run_experiment(num_trials)
print(f"총 {num_trials}번의 시도 결과, 성공 비율은 {result_rate:.2f}% 입니다.")
