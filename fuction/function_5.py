#가변 매개변수
    # 함수정의 할때 매개 변수의 개수를 지정하지 않습니다.
    # 함수내부에서는 리스트로 간주합니다. 
    # 함수를 호출하는 쪽에서는 편하게,, 1,2,3,4 --> 1,2, 3, 4,,5,1,4,5
#매개 변수로 리스트가 와도 된다. 

#가변 매개변수 - packing이 동작함.
def myFunc1(*args):
    for i in args:
        print(i)


datas = [10, 20, 50, 60]
myFunc1(datas)
myFunc1(10, 20, 50, 60)

#unpacking이 동작함. 
a, b = [10, 20]
print(f"a={a}")
print(f"b={b}")


