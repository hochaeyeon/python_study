# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 x
# 매개변수 x, 반환값 O
# 둘다 없음. 

def func3(num1, num2):
    result = num1 * num2
    return result

print(func3(5, 9))

def student_func(name, age):
    print(f"안녕하세요 이름은 {name}, 나이는 {age}입니다.")

student_func("안채연", 20)

import random
def random_func():
    return random.sample(range(100), 5)

print(random_func())

def student_func1():
    age = 20
    name = "안채연"
    print(f"안녕하세요 이름은 {name}, 나이는 {age}입니다.")

student_func1()