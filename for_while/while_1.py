# while문은 반복 횟수가 없다. 
# while 조건 :

#순환 횟수가 정해져 있지 않고, 특정 조건이 있을때 while문 사용이 좋다.

import time

count = 0
# while True:
#     count += 1
#     print(f"{count}초")
#     time.sleep(1)

#     if count % 5 == 0:
#         a = input("to be continue(Y/N)?")
#         if a.upper() == "Y":
#             continue
#         else :
#             break
        
# break 쓰지 않고 하는 방법
is_count = True
while is_count:
    count += 1
    print(f"{count}초")
    time.sleep(1)

    if count % 5 == 0:
        a = input("to be continue(Y/N)?")
        if a.upper() == "Y":
            is_count = True
        else :
            is_count = False