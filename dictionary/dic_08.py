list_a =['사과', '포도', '딸기']
#enumerate
for index, value in enumerate(list_a): #enumerate 씌우면 인덱스 번호도 앞에 붙게됨. 튜플 형태로 바뀜(인덱스, 리스트 값)
    print(f"{index} : {value}")


a, b = (0, '포도')
print(a, b)

#zip() 두개의 리스트 또는 집합을 각 원소별로 묶어준다. 
names = ['홍길동', '이순신']
ages =[25, 35]

print(list(range(3))) #리스트로 출력됨. 
print(list(zip(names, ages)))
print(dict(zip(names, ages)))

for name, age in zip(names, ages): # zip은 묶어준느 용도. 
    print(f"name:{name}, age:{age}")

#.items()
dict_1 = {'취미':'수영', '좋아하는 음식':'떡볶이'}
print(f"dict_1 = {dict_1}")
print(f"keys = {dict_1.keys()}")
print(f"values = {dict_1.values()}")
print(f"items = {dict_1.items()}")