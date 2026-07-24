def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_list = list(letters)
    sentence = sentence.lower()
    for letter in letters_list:
        if letter in sentence:
            pass
        else:
            return False
    return True