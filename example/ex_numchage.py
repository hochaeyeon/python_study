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


start = 1
end = 10    
print(get_data(start, end))

