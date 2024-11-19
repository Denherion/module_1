import random

def random_code():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(numbers)
    return n

def exception_(first, second):
    number = True
    for z in range(0, len(pin_code)):
        if (int(pin_code[z]) == int(str(first) + str(second))
                or int(pin_code[z]) == int(str(second) + str(first))):
                number = False
    return number

result = []
rand = random_code()
pin_code = []
a = list(range(1, rand))
for i in a:
    for j in a:
        if rand % int(i + j) == 0 and i != j:
            if exception_(i, j):
                pin_code.append(str(i) + str(j))

true_number = str()
for x in range(0, len(pin_code)):
    true_number += pin_code[x]

print(rand, ' - ', true_number)