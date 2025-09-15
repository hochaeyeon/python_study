# 변수에는 하나의 값만 받을 수 있다. 
# 리스트의경우에도 변수에 하나의 주소값이 들어감. ex, list_a 0번째가 주소. 

def change(obj):
    obj[0] = 100


data = [1,2,3]
data1 = change(data)
print(data)
print('-'*10)

# list_b가 가르키는 곳도 list_a의 주소값임.
# .copy()를 하면 완전 복사되어서 별도의주소값에 list_b가 배정됨. 
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b[0] = 100
print(f"list_a = {list_a} / list_b = {list_b}")