# 클래스 - 클래스 변수, 인스턴스 변수 
# 생성자 - __init__()
# self - 인스턴스 메서드의 첫 번째 매개변수로 사용
# 메소드
# __str__() : 객체를 print()로 출력할 때 호출되는 메서드
# __eq__() : 객체가 == 연산자로 비교될 때 호출되는 메서드
# __ne__() : 객체가 != 연산자로 비교될 때 호출되는 메서드   
# __lt__() : 객체가 < 연산자로 비교될 때 호출되는 메서
# __le__() : 객체가 <= 연산자로 비교될 때 호출되는 메서드
# __gt__() : 객체가 > 연산자로 비교될 때 호출되는 메서드
# __ge__() : 객체가 >= 연산자로 비교될 때 호출되는 메서
# property, setter, deleter, getter, private --> 함수를 변수 처럼 사용 
# isinstance() 함수

# 상품관리 클래스 명 Product
# 상품명 Product_name, 가격 Product_price, 재고 Product_stock


class Product:
    count = 0
    def __init__(self, name, price, stock):
        self.id = Product.count
        Product.count += 1
        self.name = name
        self.price = price
        self.stock = stock
    
    @property
    def price(self):
        return self._price  
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("가격은 음수일 수 없습니다.")
        self._price = value     

    @property
    def stock(self):
        return self._stock      
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("재고는 음수일 수 없습니다.")
        self._stock = value
        

    def __str__(self): # 객체 자체가 출력문으로 감싸질때 결과가 출력되는 함수 
        print(f"상품명 : {self.name}, 가격 : {self.price}, 재고 : {self.stock}")
    
    def __eq__(self, other):
        return self.stock == other.stock
Products = [Product("노트북", 100000, 10), Product("스마트폰", 200000, 50), Product("냉장고", 300000, 30)]

# 노트북 가격을 20% 인하
#Products[0].price = Products[0].price * 0.8
for p in Products:
    if p.name == "노트북":
        p.price = p.price * 0.8
    elif p.name == "스마트폰":
        p.price = p.price * 1.1

# 스마트폰 가격을 10% 이상
#Products[1].price = Products[1].price * 1.1

# 제품 출력



# 제품 추가
new_product = Product("에어컨", 400000, 20)
Products.append(new_product)
for p in Products:
    p.__str__()
# 제품 삭제

del_product = "에어컨"
for index, p in enumerate(Products):
    if p.name == "에어컨":
        del Products[index]
        break
# 현재 모든 제품의 수량


sum = 0
for p in Products:
    sum += p.stock

print(sum)