# list_b = [1,2,1,1,4,5,3]
# list_a = set(list_b)

# for i in list_a:
#     print(f'{i}, {list_b.count(i)}')

# for i in list_a:
#     print(i)

# str = input("값을 입력하시오")
# str_result = ''
# for i in str:
#     print(i)
#     print(i.lower())
#     # if i != i.lower:
#     #     str_result += i.lower
#     # else:
#     #     str_result += i.upper

# print(str_result)

# print("오디" + "오")
# print("" + "오")

# a = int(input())

# if a%2 == 0:
#     print('100 is even')
# else:
#     print('1 is odd')

# def solution(my_string, overwrite_string, s):
#     answer = ''
#     for i in range(s, len(overwrite_string)):
#         my_string[i] = overwrite_string[i-s]
#     return my_string        
my_string = "He11oWor1d"
s = 2
overwrite_string = "lloWorl"
print(my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):])
#print(solution(my_string, overwrite_string, 2))
