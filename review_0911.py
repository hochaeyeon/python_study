# 딕셔너리
    # .iteam() .keys() .values()
dict_1 = {'국어':100, '수학':70, '영어':60}
# print(type(dict_1))
# # iteams 는 dic_items라는  타입임. list[(튜플)] 형태인데 여기에 list를 붙이면 list형태로 바꿔 쓸 수 잇음. 
# # 요소는 (key, value) 튜플

# # 정렬
#     # sorted()
# print(type(dict_1.items()))
# print(sorted(dict_1.items(), key=lambda data: data[0]))
# print(sorted(dict_1.items(), key=lambda data: data[1]))
# print(sorted(dict_1.items(), key=lambda data: data[1], reverse=True))
# max
    # max()
scores = {"alice" : 85, "bob":92, "charlie":78}
print(max(scores))
print(scores.items())
print(max(scores, key=scores.get)) #get 메소드는 딕셔너리에만 붙어서 사용이 가능함.
print(scores["bob"]) # key값이 주어지면, value값이 나온다. 
print(scores[max(scores, key=scores.get)])
#print(scores[max(scores, key=scores.get)))
# enumerate
    # 순환문에서 리스트를 감싸면 (인덱스, 리스트의 값)
fruits = ["사과", "배", "포도"]
for index,fruits in enumerate(fruits):
    print(index,fruits)


# zip()
    # 여러개의 자료 구조 iterable 들을 각 원소를 쌍으로 하는 집합 
    # (1, 2), ('사과', '배')
    # [(1, '사과'), (2, '배'),]

    numbers = [1, 2, 3]
    fruits = ["사과", "배", "포도"]

    print(list(zip(numbers,fruits)))
    for index, value in zip(numbers, fruits):
        print(f"index : {index} , value : {value}")
# map()
    # 함수명, iterable한 객체의 각 요소에 특정 함수를 적용 
    # map(int, ['1', '2']) -> [1, 2]

str_num = ["1", "2", "3"]

int_nums = list(map(lambda data: data*2, str_num))
print(int_nums)

# 숫자 한번에 개수 세는 도구

import collections 

dates = [1,1,1,1,3,3,3,4,4,4,4]
print(collections.Counter(dates))