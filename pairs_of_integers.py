def generate_pairs(n) -> list:

    result_list = []

    for i in range(n+1):
        for j in range(n+1):
            result_list.append([i,j])

    return result_list

print(generate_pairs(2))

def generate(n) -> list:
    return [[i, j] for i in range(n + 1) for j in range(n + 1) if i <= j]

print(generate(2))