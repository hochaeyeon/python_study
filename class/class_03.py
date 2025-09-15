class People():
    def __init__(self):
        self.name = None
        self.age = None
        self.addr = None
        print("생성자 호출")

# print("객체 생성 전")
# h1 = People() 
# print("객체 생성 후")
# print(h1.addr)
# h2 = People()
# print(h2.addr)

# 생성자 개념 정리하기 
class product():
    serial_num = 0
    def __init__(self):
        product.serial_num += 1
        self.serial_num = product.serial_num
        self.name = None

tv = product()
tv1 = product()
tv2 = product()
