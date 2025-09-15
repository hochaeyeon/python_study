# 가위 바위 보 게임 
# 인간이 숫자를 입력
# 승패 기록
import random
import game_fuc

# end_point = True
# count = 0
# hum_win = 0
# comp_win = 0
# while end_point:
#     count += 1
#     computer = random.randint(1,3)
#     if computer == 1:
#         computer = "가위"
#     elif computer == 2:
#         computer = "바위"
#     elif computer == 3:
#         computer = "보"


#     # 컴퓨터 1 == 가위 / 2 == 바위 / 3 == 보
#     hum = input("가위, 바위, 보 중에서 입력하시오 : ")
#     print(f"컴퓨터 : {computer}")
#     if (computer == "가위" and hum == "바위") or (computer == "바위" and hum == "보") or (computer == "보" and hum == "가위"):
#         print("이겼습니다. ")
#         hum_win += 1
#     elif(computer == "가위" and hum == "보") or (computer == "바위" and hum == "가위") or (computer == "보" and hum == "바위"):
#         print("졌습니다.")
#         comp_win += 1
#     else:
#         print("비겼습니다.")
    
#     print(f"인간 승:{hum_win} / 컴퓨터 승:{comp_win}")
#     print("-"*30)
#     print()

#     if count % 3 == 0:
#         ans = input("계속 하시겠습니까 ? (Y/y)").upper()
#         if ans != "Y":
#             end_point = False


end_point = True
count = 0
hum_win = 0
while end_point:
    count += 1
    computer_random = random.randint(1,3)
    computer = game_fuc.game_define(computer_random)
    hum_win += game_fuc.game(computer, hum_win)
    print(f"인간 승 : {hum_win}")
    end_point = game_fuc.game_count(count)
    