def is_pangram(st: str) -> bool:

    return True if 26 == len(set(''.join(char for char in st if char.isalpha()).lower())) else False


print(is_pangram('The quick brown fox jumps over the lazy dog.'))