#사용자 입력 처리 함수
#함수 이름 get_data()
#파라미터
    # start : 시작값
    # end : 종료값
    # input_str : 가이드문구

#사용자 입력은 input
# return 정수로 변환된 입력값



def get_data(start, end):
    while True:
            try :
                input_str = int(input("정수를 입력하세요 : "))
                if start<= input_str <=end:
                    return input_str
                    break
                else:
                    raise ValueError("out of range")
            except Exception as e:
                print(f"예외 : {e}")  


# 랜덤 정수 선택
import random as r

start, end = 1, 100
com_num = r.randint(start, end) # 랜덤 정수 - 컴퓨터 선택한 값, 
count = 0
list_num = []
list_result = []
# while True:
#     hum_num = get_data(start, end)
#     list_num.append(hum_num)
#     count += 1
#     if com_num > hum_num:
#         print("작다")
#         list_result.append("작다")
#     elif com_num < hum_num:
#         print("크다")
#         list_result.append("크다")

#     else:
#         print(f"{count}번 만에 맞췄다. ")
#         list_result.append("정답")
#         break

list_r = []
while True:
    hum_num = get_data(start, end)
    list_num.append(hum_num)
    count += 1
    if com_num > hum_num:
        print("작다")
        list_r.append((hum_num,"작다"))
    elif com_num < hum_num:
        print("크다")
        list_r.append((hum_num,"크다"))
    else:
        print(f"{count}번 만에 맞췄다. ")
        list_r.append((hum_num,"정답"))
        print("-" * 30)
        for value, result in list_r: # 튜플로 받아오기 
            print(f"내가 선택한 숫자 : {value} => 결과 : {result}")
        break

#게임 
#human > computer 크다
#human < computer 작다
#human == computer 맞췄습니다.

