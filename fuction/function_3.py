# 다양한 매개변수
    # 기본 매개변수 default parameter

def myAdd(num1, num2 = 10): # 기본 매개 변수 
    return num1 + num2

result = myAdd(10) # 포지셔널 파라미터
print(f"result = {result}")
