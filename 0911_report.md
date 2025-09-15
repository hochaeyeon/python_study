# 딕셔너리
    # .iteam() .keys() .values()
# 정렬
    # sorted()
# max
    # max()
# enumerate
    # 순환문에서 리스트를 감싸면 (인덱스, 리스트의 값)
# zip()
    # 여러개의 자료 구조 iterable 들을 각 원소를 쌍으로 하는 집합 
    # (1, 2), ('사과', '배')
    # [(1, '사과'), (2, '배'),]
# map()
    # 함수명, iterable한 객체의 각 요소에 특정 함수를 적용 
    # map(int, ['1', '2']) -> [1, 2]

# 숫자 한번에 개수 세는 도구
    '''
    import collections 
    dates = [1,1,1,1,3,3,3,4,4,4,4]
    print(collections.Counter(datas))
    '''

# 기본 매개변수가 가변 매개변수보다 앞에 올때 기본 매개변수에 주어진 기본값의 의미는 사라짐. 