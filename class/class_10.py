# 숫자 맞추기 게임 
# 규칙은 
# 1. 1~100 사이의 숫자 중 하나를 컴퓨터가 선택한다.
# 2. 사용자는 숫자를 추측하여 입력한다.
# 3. 컴퓨터는 사용자가 입력한 숫자가 정답보다 높은지, 낮은지, 맞는지를 알려준다.
# 4. 사용자가 정답을 맞출 때까지 반복한다.
# 5. 사용자가 정답을 맞추면 몇 번 만에 맞췄는지 출력한다.
# 6. 이러한 규칙을 클래스로 구현합니다.

import random
class NumberGuessingGame:
    def __init__(self):  # 클래스 만들때는 생성자를 먼저 만들어야한다. 
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("숫자가 범위를 벗어났습니다. 다시 시도하세요.")
            except ValueError:
                print("유효한 숫자를 입력하세요.")

    def play(self):
        print("숫자 맞추기 게임에 오신 것을 환영합니다!")
        while True:
            user_guess = self.get_user_guess()
            self.attempts += 1

            if user_guess < self.number_to_guess:
                print("더 높은 숫자입니다.")
            elif user_guess > self.number_to_guess:
                print("더 낮은 숫자입니다.")
            else:
                print(f"축하합니다! {self.attempts}번 만에 맞추셨습니다.")
                break

NumberGuessingGame().play() 