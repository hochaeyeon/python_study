list_a = [1, 2, 3]
print(f"type(list_a) = {type(list_a)}")
tuple_a = (10, 20, 30)
print(f"type(tuple_a) = {type(tuple_a)}")

print("-"*30)
print()
tuple(list_a) # 원본은 바뀌지 않지만, 튜플 형태로 반환함. 
print(f"type(list_a) = {type(list_a)}") 
print(type(tuple(list_a)))
print("-"*30)
print()
 
list_a = tuple(list_a) # list_a가 튜플로 완전 change
print(f"type(list_a) = {type(list_a)}")
