my_bag = {"필통" : "파란색","공책" : "수학 공책","지갑": "분홍색"}

print(my_bag)

# 가방에서 필통을 꺼내서 출력
print(f"my_bag = {my_bag["필통"]}")
# 가방에서 공책을 꺼내서 출력
print(f"my_bag = {my_bag["공책"]}")
# 지갑이 오래되서 "가죽 지갑"변경
# 물통을 추가 하얀색
# 공책을 다써서 버려


# 업데이트
my_bag['지갑'] = '가죽 지갑'
print(f'my_bag = {my_bag}')

# 추가 : 업데이트랑 같은 방향
my_bag['물통'] = '하얀색'
print(f'my_bag = {my_bag}')

# 삭제
del my_bag["공책"]
print(f'my_bag = {my_bag}')

# 순환문과 연결
for i in my_bag:
    print(f"key = {i} value = {my_bag[i]}")

