# remove

list_a = [3, 2, 1, 2]

# for i in list_a:
#     if i == 1:
#         list_a.remove(i)

print(list_a)

# list_b = []
# for i in list_a:
#     if i != 1:
#         list_b.append(i)

# list_a = list_b
# print(list_a)

#발상의 전환( 뒤에서 부터 카운팅 )
for i in range(len(list_a)-1, -1, -1):
    print(i)
    if list_a[i] == 1:
        del list_a[i]
  
print(list_a)

#remove 사용할때 remove한 대상이 없으면 오류 뜸. 조건문 붙여주는게 좋음
list_a.remove(3)
print(list_a)

#break 불필요한 순환 제거를 위해서 
#for 문안에서는 리스트를 변경 안되도록 해야한다. 

