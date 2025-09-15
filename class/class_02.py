class People():
    def make_instance(self):
        self.name = None
        self.age = None
        self.addr = None

h1 = People() # people에서 self가 h1. 
h1.make_instance() # 함수를 실행해줘야함. 
print(h1.addr)
h2 = People()
print(h2.addr)