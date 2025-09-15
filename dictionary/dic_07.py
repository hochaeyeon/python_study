# 딕셔너리의 성질을 이용한 리스트의 요소를 카운트
# max함수를 이용해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 키를 return 
# 메소드.get() -> 값 반환 , 사용해봄. (메소드)

# 키를 이용해서 값을 가져오는 방법
dict_1 = {'사과' : 10, '포도' : 20}
# 포도의 값
print(dict_1['포도']) # 인덱싱 방식 없으면 keyerror 발생
print(dict_1.get('포도')) #메소드 이용하는 방식 없으면 None 
print(dict_1.get('포도', 0)) #원래 딕셔너리에 있으면 기존 값으로 출력
print(dict_1.get('파인애플', 0)) #딕셔너리에 없으면 설정한 값(0)으로 출력
print(dict_1)

# 자료구조에서 가장 큰 값을 찾는 함수 -> 내장함수 (max)
print(max([1,5,2,4,8,7,1,5,4]))
dict_1 = {'국어' : 80, '영어' : 100}
print(max(dict_1, key=dict_1.get))


#정렬
list_1 = [5, 2, 1, 3]
print(sorted(list_1, reverse=True))

dict_1 = {'국어' : 80, '국사' : 100, '수학' : 90}
print(sorted(dict_1)) # key순으로 정렬한다. 
print(sorted(dict_1, key=dict_1.get, reverse=True)) #value 순으로 정렬 , revers = True 하면 내림차순, 

