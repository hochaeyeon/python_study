# 다양한 매개변수
    # 기본 매개변수 default parameter

def myAdd(num1, num2, num3=10): # 기본 매개 변수는 항상 마지막에 와야한다. 다 오는것도 가능
    return num1 + num2 + num3

result = myAdd(10, 20) # 포지셔널 파라미터
print(f"result = {result}")
