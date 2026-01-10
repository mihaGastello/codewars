def service(score: str) -> str:

    sum_int = sum([int(x) for x in score.split(":")])

    if sum_int >= 40:
        return "first" if sum_int % 4 < 2 else "second"
    else:
        return "first" if (sum_int + 10) % 10 < 5 else "second"












