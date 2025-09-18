# # 직원 - ID, 이름, 기본급
# class Employee:
#     def __init__(self, id, name, base_salary):
#         self.id = id
#         self.name = name
#         self.base_salary = base_salary
#         self._base_salary = base_salary
#     @property
#     def base_salary(self):
#         return self._base_salary
#     @base_salary.setter

#     def base_salary(self, money):
#         if money > 0:
#             self._base_salary = money
#         else:
#             raise ValueError("금액은 양수 입니다. 마이너스 불가")
#     def emy(self):
#         print("직원 클래스 ")

#     def __str__(self):
#         return f'{self.name} : {self.id}, {self.base_salary}' 
# # 정규직 FullTimeEmployee
# # 계약직 PartTimeEmployee
# # 정규직, 계약직, 인턴 

# class FullTimeEmployee(Employee):
#     def __init__(self, id, name, base_salary, bonus):
#         super().__init__(id, name, base_salary)
#         self.bonus = bonus
    
#     def fte(self):
#         print("정직원 클래스 ")
    
#     def __str__(self):
#         return super().__str__()+ f', {self.bonus}'

# class partTimeEmployee(Employee):
#     def __init__(self, id, name, hourly_rate, hours):
#         super().__init__(id, name, 0)
#         self.hourly_rate = hourly_rate
#         self.hours = hours
    
#     def pte(self):
#         print("계약직 클래스 ")
    
    
#     def __str__(self):
#         return f'{self.name} {self.id} {self.hourly_rate} {self.hours}'

# class Intern(Employee):
#     def __init__(self, id, name, fixed_salary):
#         super().__init__(id, name, 0)
#         self.fixed_salary = fixed_salary
    
#     def itn(self):
#         print("인턴 클래스 ")
        
    
#     def __str__(self):
#         return f"{self.name} {self.id} {self.fixed_salary}"

# # 정규직 직원, 계약직, 인턴을 모두저장하는 리스트 
# emp = [FullTimeEmployee(), 
#        partTimeEmployee(), 
#        Intern(),
#        FullTimeEmployee()]

# for i in emp:

# 직원 Employee - 아이디,이름,기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary  # private의 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, money):
        if money > 0:
            self._base_salary = money
        else:
            raise ValueError('금액은 양수입니다. 마이너스 불가')
    def emp(self):
        print('직원클래스')

    def __str__(self):
        return f'{self.name} : {self.id}, {self.base_salary}'
    
# 정규직 FullTimeEmployee- 보너스
class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary,bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus
    # bonus도 마이너스 입력 불가        
    def __str__(self):
        return super().__str__() + f', {self.bonus}'
    def emp(self):
        print('정규직 클래스')
# 계약직 PartTimeEmployee- 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id, name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours
    # hourly_rate  hours  : getter setter
    def __str__(self):
        return f'{self.name} {self.id} {self.hourly_rate} {self.hours}'
    def emp(self):
        print("계약직 클래스")

# 인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name, 0)
        self.fixed_salary = fixed_salary
    def __str__(self):
        return f'{self.name} {self.id} {self.fixed_salary}'
    def emp(self):
        print('인턴클래스')

# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
# emp = [
#     FullTimeEmployee(),
#     ...
#     ...
#     ...
#     ...
#     ..
# ]
# emp에 들어있는 직원이 각각 어떤클래인지 순환을 이용해서 각 클래스의 int,pte 메소드 호출


Employee = [FullTimeEmployee(1, "홍길동", "200000", "200000"), 
       PartTimeEmployee(2, "강감찬", "10000", "20"), 
       Intern(3, "이순신", "100000"),
       FullTimeEmployee(1, "박보검", "500000", "500000")]

# emp()가 각class에 따라 함수값이 달라진다. 다형성  모든 클래스에 같은 이름의 메소드가 있을때 
# emp에 들어있는 직원이 각각 어떤클래인지 순환을 이용해서 각 클래스의 int,pte 메소드 호출
for i in Employee:
    i.emp()

