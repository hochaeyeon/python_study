# 튜플
# count, index 두가지 기능 밖에 없음. 튜플은 읽기 전용이다. 
tuple_01 = (1, 2, 3, 4, 1, 2, 3, 4, 5, 1)
print(tuple_01[0])
#tuple_01[0] = 100 # 에러 발생.
print(tuple_01.count(1)) # 1을 count했음. 
print(tuple_01.index(4)) # 4의 인덱스 

# 튜플 vs 리스트는 서로 변경이 가능하다. 
# 튜플 데이터를 리스트로 만들 수 있고, 리스트를 튜플로 만들 수 있다.

 