import random

def game_define(computer):
    if computer == 1:
        return "가위"
    elif computer == 2:
        return "바위"
    elif computer == 3:
        return "보"


def game(com_choice, human_win):
    # 컴퓨터 1 == 가위 / 2 == 바위 / 3 == 보
    human_choice = input("가위, 바위, 보 중에서 입력하시오 : ")
    print(f"컴퓨터 : {com_choice}")

    if com_choice == human_choice:
        print('비겼습니다.')
        return 0
    else:
        if (com_choice == "가위" and human_choice =="바위") or \
            (com_choice == "바위" and human_choice =="보") or \
            (com_choice == "보" and human_choice =="가위"):
            print("당신이 이겼습니다.")
            human_win = 1
            return human_win
        else:
            print("당신이 졌습니다.")
            return 0


def game_count(count):
    if count % 3 == 0:
        ans = input("계속 하시겠습니까 ? (Y/y)").upper()
        if not ans == "Y":
            return False
    return True
