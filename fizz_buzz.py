from typing import List

def fizzbuzz(n) -> List:
    result: List = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


def fizzbuzz2(n) -> List:
    return [
        "FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i for i in range(1, n + 1)
    ]

print(fizzbuzz(16))
print(fizzbuzz2(16))