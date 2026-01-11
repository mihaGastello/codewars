def pig_it(text):
    words = text.split()
    new_words = []
    for word in words:
        if word.isalpha():
            letters = (list(word))
            first = letters.pop(0)
            letters.append(first)
            letters.append("ay")
            new_word = ''.join(letters)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return ' '.join(new_words)


def pig_it2(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it("Hello world !"))
print(pig_it2("Hello world !"))