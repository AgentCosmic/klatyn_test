def fibonacci(end):
    if end < 0:
        raise Exception('Must be more than 0')
    if end < 2:
        return 0
    if end < 3:
        return 2
    a = 1
    b = 2
    c = a + b
    total = 2
    while b <= end:
        if c % 2 == 0:
            total += c
        c = a + b
        a = b
        b = c
    return total
