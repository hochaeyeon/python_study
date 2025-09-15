#정렬
list_a = [('국어', 100),('영어', 95),('수학',85)]
# key는 정렬 기준으로 정한느 역할
# lambda에서 매개 변수 data는 list_a의 데이터
print(sorted(list_a, key = lambda data: data[1])) # key = 는 기준을 나타내는거 

dict_1 = {'국어' : 100, '영어' : 95, '수학' : 88}
print(sorted(dict_1.items(), key=lambda data: data[1]))
# items : for 반복문에서 key와 value를 동시에 꺼낼때 사용 (읽기 전용)

# map :자료구조의 각 요소의 특정 함수를 적용한 것. 
str_num = ['1', '10', '100']