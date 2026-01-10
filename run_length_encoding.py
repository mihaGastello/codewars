def run_length_encoding(s: str) -> list:
    s = s + "0"
    result_list = []
    counter: int = 1
    checking_char = "0"

    for char in s:
        if char == checking_char:
            counter += 1
        else:
            if checking_char != "0":
                result_list.append([checking_char, counter])
            checking_char = char
            counter = 1

    return result_list


print(run_length_encoding("adceeerrq"))