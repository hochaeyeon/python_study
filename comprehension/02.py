list_1 = []
[i for i in range(5) if i%2 == 0] #조건은 뒤에 붙는다. 

list_1 = [1,2,3,1,2,3,5,4,8]
# 값 2에 해당하는 인덱스를 찾아서 리스트로 반환 
# [1, 4]

print([idx for idx, value in enumerate(list_1) if value==2]) # 조건 단독으로쓸때는 뒤에오고, if-else면 앞에 온다. 

age = 18
if age >= 18:
    print('성인')
else:
    print('학생')

print("성인" if age >= 18 else "미성년")
print(["성인" if i >= 18 else "미성년" for i in list_1])

#짝수는 1로 홀수는 0으로 바꿔라
list_2 = [1,2,1,5,3,1,54]
new_list_2 = []
for a in list_2:
    if a%2 == 0:
        a = 1
        new_list_2.append(a)
    else:
        a = 0
        new_list_2.append(a)

print(new_list_2)

