
# map :자료구조의 각 요소의 특정 함수를 적용한 것. 
str_num = ['1', '10', '100']

print(list(map(int, str_num))) # 각 요소들을 int형으로 다 바꿈. 

score = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요 ')
print(score) # 문자열로 들어옴. 
score = score.split()
print(score)  # 문자열을 잘라서 리스트에 넣어줌. 

kor, eng, math = map(int, score)
print(kor + eng + math)

list_2 = [10, 20, 30]
#각 원소에 x2 

def test(data):
    return data*2

print(list(map(lambda data : data*2 , list_2)))
