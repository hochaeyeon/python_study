# 부분 문자열 이어 붙여 문자열 만들기 

# def solution(my_string, parts):
#     answer = ''
#     for s, (x, y) in zip(my_string, parts):
#         answer += s[x:y+1]
    
#     return answer

# def solution_1(my_string, parts):
#     return ''.join(s[x:y+1] for s, (x, y) in zip(my_string, parts))

# my_string = ["progressive", "hamburger", "hammer", "ahocorasick"]
# parts = [[0, 4],[1, 2],[3, 5],[7,7]]

# print(solution_1(my_string, parts))

# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a, b, c, d):
    dice = [a, b, c, d]
    unique_dice = set(dice)
    
    if len(unique_dice) == 1:  # 네 주사위가 모두 같음
        p = dice[0]
        return 1111 * p
    elif len(unique_dice) == 2:
        p = max(unique_dice, key=dice.count)
        q = min(unique_dice, key=dice.count)
        if dice.count(p) == 3:  # 세 주사위가 같고 하나가 다름
            return (10 * p + q) ** 2
        else:  # 두 쌍이 각각 같음
            return (p + q) * abs(p - q)
    elif len(unique_dice) == 3:  # 두 주사위가 같고 나머지 두 개는 다름
        for num in unique_dice:
            if dice.count(num) == 1:
                q = num
            elif 'p' not in locals():
                p = num
            else:
                r = num
        return q * r
    else:  # 네 주사위가 모두 다름
        return min(dice)