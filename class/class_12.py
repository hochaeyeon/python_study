#클래스 콜백함수
#__eq__() : 객체가 == 연산자로 비교될 때 호출되는 메서드
#__ne__() : 객체가 != 연산자로 비교될 때 호출되는 메서드   
#__lt__() : 객체가 < 연산자로 비교될 때 호출되는 메서드
#__le__() : 객체가 <= 연산자로 비교될 때 호출되는 메서드
#__gt__() : 객체가 > 연산자로 비교될 때 호출되는 메서드
#__ge__() : 객체가 >= 연산자로 비교될 때 호출되는 메서드

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"이름: {self.name}, 점수: {self.score}" # 자체 프린트할때
    
    def __eq__(self, other):
        print({self.name} == {other.name})
        print("__eq__() 호출됨")

s1 = Student("홍길동", 90)
s2 = Student("김철수", 80)
print(s1) 
print(s2) # __str__() 호출됨
s1 == s2  # __eq__() 호출됨