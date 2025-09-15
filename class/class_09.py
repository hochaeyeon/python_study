#가위 바위 보 게임
# 사용자에게 가위, 바위, 보 중 하나를 입력받아 컴퓨터와 대결하는 게임을 만드세요.
# 컴퓨터는 랜덤으로 가위, 바위, 보 중 하나를 선택합니다.
# 사용자가 이기면 "이겼습니다!", 지면 "졌습니다!", 비기면 "비겼습니다!"를 출력합니다.
# 가위는 1, 바위는 2, 보는 3으로 표현합니다.
# 이러한 규칙을 클래스로 구현합니다. 
# 게임이 끝나면 계속할지 물어본다. 사용자가 종료를 입력하면 게임을 종료한다. 
import random
class RPSGame:
    def __init__(self):
        self.choices = {1: "가위", 2: "바위", 3: "보"}

    def get_computer_choice(self):
        return random.randint(1, 3)

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if choice in self.choices: # 딕셔너리를 순환문에 넣으면 key값 비교함. 
                    return choice
                else:
                    print("잘못된 입력입니다. 다시 시도하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def determine_winner(self, user, computer):
        if user == computer:
            return "비겼습니다!"
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            return "이겼습니다!"
        else:
            return "졌습니다!"

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"컴퓨터는 {self.choices[computer_choice]}를 선택했습니다.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            again = input("계속하시겠습니까? (y/n): ").strip().lower()
            if again != 'y':
                print("게임을 종료합니다.")
                break

RPSGame().play()
