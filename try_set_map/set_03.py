# 집합 연산이 가능
import random

list_a = random.sample(range(11), 7)
list_b = random.sample(range(11), 7)

list_c = []
for _ in range(7):
    list_c.append(random.randint(0, 10))

# 교집합
    # 연산자 |  (파이프 연산자) ---> or
    # 메서드 .union() # .붙어 있으면 메서드 / 독립적으로 존재하면 함수  

# 합집합
# 차집합

