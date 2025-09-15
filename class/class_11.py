#isinstance() 함수
# 객체가 특정 클래스의 인스터스(객체)인지 확인한다. 
# 사용하는 이유
# 1. 타입학인 
# 2. 다형성 지원 
class Student:
    def study(self):
        print("공부 중 입니다.")
class Teacher:
    def teach(self):
        print("가르치는 중 입니다.")    

# 리스트에 어떤 객체가 있는지 모를때 isinstance()로 확인한다.
peoples = [Student(), Teacher(), Student()]
if isinstance(peoples[0], Student):
    peoples[0].study()
else:
    peoples[0].teach()
    