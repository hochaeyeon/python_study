class StudentMng():
    name = "홍길동"

s1 = StudentMng()
s2 = StudentMng() # 객체 별로 독립적으로 존재하는 변수를 인스턴스 변수라고 함. 
s3 = StudentMng()

data1,data2 = 1,2

s1.name = data1 # 인스턴스 변수

s1.age = 12 # 기존 클래스에 없는 변수 지정해주면 새로 생김. # 클래스 변수
StudentMng.name = data2
print(s1.name, s2.name, s3.name)

# 클래스 변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 제 할당받으면 해당 객체는 더 이상 참조하지 않는다. 


# 클래스 변수 vs 인스턴스 변수     

