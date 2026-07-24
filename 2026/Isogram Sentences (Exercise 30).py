def is_isogram(phrase):
    phrase = phrase.lower()
    for letter in phrase:
        if letter.isalpha():
            if phrase.count(letter) > 1:
                return False
    return True