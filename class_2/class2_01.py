# 상속의 정의

# 부모클래스
class Parents:
    def __init__(self, name):
        self.p_name = name
        print("부모 생성자")
    def parents_metod(self):
        print("부모클래스 매소드")
    
class Child(Parents):
    def __init__(self, name, age):
        Parents.__init__(self, name) # 부모 생성자 불러오기 
        self.age = age
        print("자식 생성자")
    def Child_method(self):
        print("자식클래스 메소드")


c = Child("홍길동", 20) # 무조건 생성자 호출됨 , 생성자 없으면 기본 껍데기가 생성됨. 
print(c.p_name)
c.Child_method()
c.parents_metod() #부모의 메소드도 사용 가능. 
  