#number_input_a = int(input("정수 입력>"))

# print("원의 반지름 :", number_input_a)
# print("원의 둘레 :", 2 * 3.14 * number_input_a)
# print("원의 넓이 :", 3.14 * number_input_a * number_input_a)

# n = 3.14
# print(int(n))

# 오류는 피해가는 행위 -> 예외 처리 
try:
    num1, num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력").split())
    calc_list = [num1+num2, num1-num2, num1*num2, num1/num2]

# print(f'{num1} + {num2} = {calc_list[0]}')
# print(f'{num1} + {num2} = {calc_list[1]}')
# print(f'{num1} + {num2} = {calc_list[2]}')
# print(f'{num1} + {num2} = {calc_list[3]}')

    print("1. 더하기", end='\t')
    print("2. 빼기", end='\t')
    print("3. 곱하기", end='\t')
    print("4. 나누기")
    choice = int(input("원하는 결과를 입력하세요 : "))
    print(f"결과는 = {calc_list[choice-1]}")
except:
    print("오류 발생") #에러가 날때 출력함. 

#현업에서는 에러를 파일에 입력함. (로그 라이브러리)
#try except finally 

# ex1

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤 입니다.")
    except:
        print("except 실행되었습니다.")
    finally:
        print("finally 실행되었습니다.")
    print("test() 함수의 마지막 줄 입니다.")

    # try내 return이 있음. 그래도 finally는 무조건 실행되어야 한다.
test()