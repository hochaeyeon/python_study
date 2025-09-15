try:
    print("정상코드")
    print("예외발생")
    raise "내가 발생시킨 오류" # raise 키워드 : 예외를 강제로 발생 시킴. 
    #raise ValueError("테스트")

except Exception as e:
    print(f"에러 : {e} {e.__class__} {e.__class__.__name__}")



#try-except에서 except에서 pass를 쓰는 경우 ..?