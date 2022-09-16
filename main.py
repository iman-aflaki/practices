import math
def ishappy(num):
    past = set()
    while num != 1:
        num = sum(int(i)**2 for i in str(num))
        if num in past:
            return False
        past.add(num)
    return True

counter = 0
number = 1
list = []
while counter <= 20:
    if ishappy(number):
        list.append(number)
        counter += 1
        number += 1
    else:
        number += 1
print(list)
