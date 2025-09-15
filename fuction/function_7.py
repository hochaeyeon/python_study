import time


def display_second(count):
    count += 1
    print(f"{count}초")
    time.sleep(1)
    return count

def five_count(count):
    if count % 5 == 0:
        user_input = input('To be Continue(Y/y)').upper()
        if not user_input == 'Y':
            return False
    
    return True
    
count = 0
is_continue = True
while is_continue:
    count = display_second(count)
    is_continue = five_count(count)
    