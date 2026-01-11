def find_outlier(integers):
    evens = [num for num in integers if num % 2 == 0]
    odds = [num for num in integers if num % 2 == 1]

    return odds[0] if len(odds) < len(evens) else evens[0]

    # if len(evens) == 1:
    #     return evens[0]
    # if len(odds) == 1:
    #     return odds[0]

print(find_outlier([1, 4, 8, 6]))
