# 투표는 순환문을 이용해서 유권자가 10이라면 10번 순환하면서 후보자(1~5) 선택
# [1, 1, 2, 3, 4, 1, 5, 1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
# 1. 딕셔너리
# 2. count 함수 사용

cadidate = ['홍길동', '이순신', '강감찬', '율곡', '심사임당']
# vote = []
counts = 10
c = 0
result = {}

#2.
# result = []
# while c < 10:
#     num = int(input("투표를 하세요(1~5) : "))
#     vote.append(num)
#     for i in range(1, 6):
#         result.append(vote.count(i))
    
#     c+= 1

# print(cadidate[max(result)+1])


vote = [1, 1, 2, 3, 4, 1, 5, 1]
#dic 기능 이용
for i in vote:
    if i in result: #result가 가지고 있는 key중에서 
        result[i] += 1
    else:
        result[i] = 1

print(f"result = {result}")

# get은 값을 리턴하는 함수  딕셔너리변수['키값']없으면 에러
# 딕셔너리변수.get('키값') 없으면 None
print(max(result, key = result.get)) # result.get 을 하면 키 값들 가지고 max값 구하기 

def test(data, key):
    for i in data:
        key(i)