list_a = [100,500,10,500,100,50,500,10]
# 저금통에 있는 동전의 종류 10, 50, 100, 500

#set 중복을 제거함. 
set_a = {1, 2, 3, 1, 2, 3, 2}
print(f"set_a = {set_a}") # 출력은 set_a = {1, 2, 3}

print()
list_a = set(list_a)

set_2 = {1,2,3}
set_2.add(4) # 값 추가할때
print(set_2)
set_2.update([9])# 값을 바꿀때
print(set_2)