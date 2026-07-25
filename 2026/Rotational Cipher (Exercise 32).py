def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_to_preserve = alphabet[key:]
    alphabet_to_add = alphabet[:key]
    ROT_alphabet = (alphabet_to_preserve + alphabet_to_add)
    #Now we get the ROT key String
    answer = ""

    for i in text:
        if i.lower() in alphabet:
            if i.isupper():
                letter_to_add = ROT_alphabet[alphabet.index(i.lower())]
                letter_to_add = letter_to_add.upper()
                answer += letter_to_add
            else:
                answer += ROT_alphabet[alphabet.index(i)]
        else:
            answer += i
    return answer