# from typing import Union

def divisors(num: int) -> [int] | str:

    result = [x for x in range(2, num) if num % x == 0]
    return result if len(result) > 0 else f'{num} is prime'


print(divisors(13))

# result = []
# for i in range(2, num):
#     if num % i == 0:
#         result.append(i)