# import random
# r = print(random.randint(1, 5))
# # print는 반환값이 없음. r에는 none이 들어감. 
# print(r)

# 용어 정리 
# 함수 정의 할때는 def 키워드 사용함. 
# 매개변수(parameter) - 함수가 전달 받는 값. 
# 인자(argument) - 함수를 호출할때 전달하는 값.
# 반환값 (return value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값 (return 키워드 사용)

# 함수의 구성요소
def myCalc(num1, num2):
    '''
    두 개의 값을 받아서 더하는 기능
    num1는 숫자
    num2는 숫자
    '''
    result = num1 + num2
    return result # return이 항상 있는게 아니다. 

print(myCalc(1, 2))

#1. 매개변수와 반환값이 없는 함수
def say_hello():
    print("안녕하세요")

say_hello()

# 매개 변수가 있고 반환값이 없는 함수
def say_hello(name):
    print(f'{name}님 안녕하세요')

say_hello("안채연")

import datetime
# 매개 변수 없고, 반환값 있는 함수
def get_current_time():
    return datetime.datetime.now()

print(get_current_time())

#함수를 사용하는 이유
# 1. 재사용성
# 2. 가독성 