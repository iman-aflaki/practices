import math
def ishappy(number):
    included = set()
    while number != 1:
        number = sum(int(i)**2 for i in str(number))
        if number in included:
            return False
        included.add(number)
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
