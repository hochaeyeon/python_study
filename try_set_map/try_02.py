try:
    num1, num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력").split())
    calc_list = [num1+num2, num1-num2, num1*num2, num1/num2]

    print("1. 더하기", end='\t')
    print("2. 빼기", end='\t')
    print("3. 곱하기", end='\t')
    print("4. 나누기")
    choice = int(input("원하는 결과를 입력하세요 : "))
    print(f"결과는 = {calc_list[choice-1]}")
# 에러 종류 출력해줌
except Exception as e:
    print(f"오류 발생 : {e}") #에러가 날때 출력함. 

# 특정 에러 종류 별로 출력도 가능
except ValueError:
    print("value error 발생")
print("프로그램 종료")