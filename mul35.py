import math

def find_multiple(top):
    if top < 0 or math.floor(top) != top:
        raise Exception('Not natural number')
    total = 0
    for i in range(top):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            total += i
    return total
