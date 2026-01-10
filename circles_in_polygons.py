def dont_give_me_five(start,end) -> int:
    result = []

    for i in range(start, end + 1):
        if "5" not in str(i):
            result.append(i)

    return len(result)


def dont_give_me_five2(start,end) -> int:
    return len([i for i in range(start, end + 1) if "5" not in str(i)])

print(dont_give_me_five(4, 17))
print(dont_give_me_five2(4, 17))
