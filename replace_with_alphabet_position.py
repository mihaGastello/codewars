def alphabet_position(text: str) -> str:
    result_str = ""

    for char in list(text.upper()):
        if char.isalpha():
            number = ord(char) - ord('A') + 1
            result_str += f" {number}"
    return result_str.lstrip()

print(alphabet_position("The sunset sets at twelve o' clock."))