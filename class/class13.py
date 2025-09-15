#파이썬 클래스에서 getter, setter, deleter 사용하기
import random
class Person:
    def __init__(self, name, age):
        self._name = name  # _로 시작하는 변수는 보호된 변수로 간주됩니다.
        self._age = age

#getter 호출
    @property #ㅔproperty 속성을 가지면 name이라는 메서드가 name이라는 속성처럼 동작한다.
    def name(self): # 외부에서는 변수에 값을 세팅한다고 했는데 내부에서는 함수가 돌아감. 
        return self._name

    # @name.setter
    # def name(self, value):
    #     if not value:
    #         raise ValueError("이름은 비어 있을 수 없습니다.")
    #     self._name = value

    #  직접 값이 세팅 안되고 우회적으로 할때 @property와 @setter를 사용한다. 함수를 변수처럼 쓴다. 변수처럼 함수 이름만 언급하면 될거다. 
    @property # 사용자가 함수처럼 호출하는게 아니라 속성처럼 호출하게 한다. @property 와 @setter는 쌍으로 사용된다.하나만 있으면 사용 x
    def age(self):
        return self._age
    
    @age.setter# setter 데코레이터를 사용하여 age 속성에 값을 설정하는 메서드를 정의합니다.
    def age(self, value):
        self._age = value
p1 = Person("홍길동", 25)
print(p1.age)  # getter 호출
p1.age = 30 # setter 호출
print(p1.age)  
    # @age.setter
    # def age(self, value):
    #     if value < 0:
    #         raise ValueError("나이는 음수일 수 없습니다.")
    #     self._age = value

    # @age.deleter
    # def age(self):
    #     del self._age

#getter, setter, deleter를 사용하면 캡슐화가 가능하다.
# 캡슐화 : 객체의 속성(데이터)와 메서드(함수)를 하나로 묶는 것
# 캡슐화의 장점 :
# 1. 데이터 보호 : 객체의 속성을 직접 접근하지 못하게 하여 데이터   보호
# 2. 코드 유지보수 : 객체의 내부 구현을 변경해도 외부 인터페이스는 변경되지 않음
# 3. 코드 재사용 : 캡슐화된 객체는 다른 프로그램에서 재사용 가능
# 4. 코드 가독성 : 객체의 속성과 메서드를 하나로    묶어 코드 가독성 향상    