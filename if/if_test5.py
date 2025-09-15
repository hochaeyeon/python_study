# 논리 연산자 사용
# 나이가 18이상(성인) 이면서 주민 번호를 가진 사람은 "입장 가능" " 입장 불가 "
has_id = True
age = int(input("나이 : "))

if age >= 18 and has_id:
    print("입장 가능")
else :
    print("입장 불가능")

print("종료")