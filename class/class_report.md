# 파이썬 클래스, map 함수, tuple 학습 리포트
본 리포트는 파이썬의 객체지향 프로그래밍 핵심 개념(클래스), 데이터 변환(map 함수), 불변 자료형(tuple)에 대해 학습한 내용을 정리한 문서입니다.
## 1. 클래스(Class)

클래스는 객체를 생성하기 위한 설계도이며, 관련 변수와 메서드를 하나로 묶어 관리합니다.
클래스 변수: 클래스 전체에서 공유되는 변수
인스턴스 변수: 각 객체(인스턴스)마다 별도로 존재하는 변수
생성자: `__init__()` 메서드로 객체 생성 시 초기화 작업을 수행
self: 인스턴스 메서드의 첫 번째 매개변수로, 해당 객체 자신을 가리킴
주요 메서드
    - `__str__()`: 객체를 print()로 출력할 때 호출되어 사람이 읽기 쉬운 문자열 반환
    - `__eq__()`: == 연산자 사용 시 객체의 동등성 비교
    - `__ne__()`: != 연산자 사용 시 객체의 비동등성 비교
    - `__lt__()`: < 연산자 사용 시 크기 비교
    - `__le__()`: <= 연산자 사용 시 크기 비교
    - `__gt__()`: > 연산자 사용 시 크기 비교
    - `__ge__()`: >= 연산자 사용 시 크기 비교
property, setter, getter, deleter, private: 메서드를 변수처럼 사용하거나 접근 제어를 할 수 있음
`isinstance()` 함수: 객체가 특정 클래스의 인스턴스인지 확인

### 클래스 예제
```python
class Person:
    count = 0  # 클래스 변수
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age
        Person.count += 1
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"
    def __eq__(self, other):
        return self.age == other.age
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("홍길동", 20)
p2 = Person("임꺽정", 25)
print(p1)  # __str__ 호출
print(p1 == p2)  # __eq__ 호출
print(p1 < p2)   # __lt__ 호출
print(isinstance(p1, Person))  # True
```

---

## 2. map 함수

map 함수는 반복 가능한 객체의 각 요소에 함수를 적용하여 새로운 값을 생성합니다.
대량의 데이터 변환, 전처리 등에 활용됩니다.
문법: `map(함수, 반복가능객체)`
반환값은 map 객체이므로, list 등으로 변환하여 사용합니다.

### map 함수 예제
```python
def square(x):
    return x * x
numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16]
```

---

## 3. tuple(튜플)

튜플은 여러 값을 하나의 변수에 저장할 수 있는 자료형으로, 값 변경이 불가능(immutable)합니다.
리스트와 유사하지만, 데이터 보호가 필요한 경우에 사용합니다.
인덱싱, 슬라이싱, 언패킹 등 다양한 연산이 가능합니다.

### tuple 예제
```python
t = (10, 20, 30)
print(t[0])  # 10
print(t[1:]) # (20, 30)
# 튜플 언패킹
x, y, z = t
print(x, y, z)  # 10 20 30
```

---

*작성일: 2025-09-15*
*작성자: hochaeyeon*
