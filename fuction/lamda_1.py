#람다가 사용되지 않은 상황
def add(a, b):
    return a+b

def minus(a, b):
    return a - b

def calc(func, a, b):
    return func(a, b)

print(calc(minus, 1, 2))

print(calc(lambda a,b : a+b, 1,2 ))