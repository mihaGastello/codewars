def dig_pow(n: int, p: int):

    digits = list(str(n))
    total: int = 0

    for digit in digits:
        print(digit)
        total += int(digit) ** p
        p += 1

    if total % n == 0:
        return total / n
    else:
        return -1

print(dig_pow(46288, 3))