from abc import ABC, abstractmethod

class Parents:
    def make_money(self):
        raise NotImplementedError

class Child(Parents):
    def make_money(self):
        print("장사") # 부모 클래스 메소드를 재정의한다.(override)

    def save_money(self):
        print("투자")

c = Child() # 부모의 추상메서들르 상속받으면 클래스에서 반드시 재 정의 안하면 객체 생성 불가 
c.make_money() # 다형성 #자식 클래스에서 재정의하면 예외 발생하도록 설계


