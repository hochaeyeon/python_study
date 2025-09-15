'''
stafe = {
    '홍길동' : {
        '직책' : '매니저',
        '연봉' : 200,000,000,
        '경력' : {
            '삼성전자' : 5,
            '엘지전자' : 3,
            'sk': 10
            },
            '취미' : ['낚시', '헬스', '수명', '자전거']
    }
}
'''

#학생이 가지는 과목이 3과목이고 국어 영어 수학 이렇게 점수를 관리
student1 = [100,80, 95]
student2 = [90, 65, 90]
student3 = {'국어' : 100, '영어' : 100, '수학' : 100}
student4 = {'국어' : 80, '영어' : 100, '수학' : 88}
student5 = {'국어' : 100, '영어' : 100, '수학' : 92}

element_class = [student3, student4, student5]
sum = 0
list_math = []
for student in element_class:
    sum += student["수학"]
    list_math.append(student["수학"])
print(sum)
print(list_math)