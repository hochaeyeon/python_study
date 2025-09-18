#리스트 컴프리핸션

# total = []
# for i in range(1, 11):
#     total.append(i)


print([i for i in range(1, 11)])

import random
random.randint(1, 10)

for i in range(5):
    random.randint(1, 10)

    
print([random.randint(1,10) for i in range(5)])