def high_and_low(numbers: str) -> str:
    int_list = [int(x) for x in numbers.split()]
    return f'{max(int_list)} {min(int_list)}'
