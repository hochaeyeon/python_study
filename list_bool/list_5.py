# pop과 del의 차이 
# 둘다 삭제 기능이지만, pop은 삭제된걸 반환해줌. del은 반환해주지 않음. 

import random #랜덤 라이브러리

list_a = random.sample(range(100), 5)
print(f"list = {list_a}")
print("-" * 30)
print("리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print(list_a)

list_a.append(random.randint(0, 10))
print(list_a[-1])
print(50 in list_a)
print(list_a) 

# 다 지우기
list_a.clear()