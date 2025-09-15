# and연산자 or연산자
# and : 두개의 조건이 모두 True일때만 전체 평가가 True
#~이고, ~이다.
# or : 둘 중 하나만 True면 전체 평가가 True
#~이거나 ~이다

#평균이 60 이상, 각 과목별 점수가 40 이상이면 합격(and)
# avg = 70
# score1 = 50
# if avg >= 60 and score1 >= 40:
#     print("합격")
# else:
#     print("불합격")

print(10 > 0 and 10 > 100)  # True = 1, False = 0 1x0 = 0
print(10 > 0 or 10 > 100)   # 1 + 0 = 1
# #60이상 이거나 5세 미만이면 입장료 무료(or)
# age = 65
# if age >= 65 or age <= 5:
#     print("Free")
# else:
#     print("not-Free")
