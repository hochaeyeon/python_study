
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = []

for i in range(0,3):
    list_c.append(list_a[i] + list_b[i])

print(list_c)
print("# 리스트")
print("list_a = ", list_a)
print(f"{list_a+list_b}")
print(f"{list_a*2}")
