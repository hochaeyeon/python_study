3 #kor, eng, math 각 변수를 사용자로 부터 값을 받아서
# avg 변수에 평균값을 저장하고
#조건을 평균이 60 이상이고 kor, eng, math변수의 각 값이 40이상일때만 합격출력

kor = int(input("국어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))

avg = (kor + math + eng) / 3
if avg >= 60 and kor >= 40 and math >= 40 and eng >= 40:
    print("합격")
else:
    print("불합격")