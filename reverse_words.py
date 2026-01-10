def reverse_words(text: str) -> str:
    # Разбиваем строку на символы, отслеживая пробелы
    result = []
    word = []

    for char in text:
        if char == ' ':
            # Если встретился пробел, переворачиваем накопленное слово и добавляем его + пробел
            if word:
                result.extend(reversed(word))
                word = []
            result.append(char)
        else:
            word.append(char)

    # Не забываем последнее слово, если строка не заканчивается пробелом
    if word:
        result.extend(reversed(word))

    return ''.join(result)

txt = ' miha anna  olya    rem '
print(txt)
print(reverse_words(txt))


