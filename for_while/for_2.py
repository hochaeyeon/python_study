import random

list_a = random.sample(range(100), 10)
print(list_a)
print("-"*30)

list_b = []
for i in list_a:
    if i % 2 == 0: #짝수면 
        list_b.append(i)

print(list_b)
print(len(list_b))
    
# list_a 중에 짝수만 찾아서 새로운 리스트에 저장. 
# 1. 리스트를 순환한다. 
# 2. 순환하면서 각 데이터가 짝수인지 판단한다. 
# 3. 짝수이며 미리 준비한 빈 리스트에 추가한다. 
# 4. 모든 순환이 끝나면 (for 문 끝나면) 준비한 리스트를 출력하고 len()을 이용해서 개수도 확인한다. 