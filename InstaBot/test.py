import random


already_picked_num = []


num = random.randrange(1, 15)
if num in already_picked_num:
    num = random.randrange(1, 15)
else:
    already_picked_num.append(num)
print(already_picked_num)
print(num)