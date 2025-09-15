# 학생
# 이름, 학생 정보 출력
# 변수 : 이름
# 함수 : 학생정보 출력

Students = [] # 학생 이름 저장
class Student():
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def info_student(self):
        print(f"이름 : {self.name} 나이 : {self.age}")

s1 = Student()
s1.name = '홍길동'
s1.age = 25
# 학생정보 입력
Students.append(s1)

s2 = Student()
s2.name = '이순신'
s2.age = 30
Students.append(s2)

Students[0].info_student()
