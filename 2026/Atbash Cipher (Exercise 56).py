#Maybe it was better to use a dict

plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"
numbers = "0123456789"
plain = list(plain)
cipher = list(cipher)
numbers = list(numbers)

def encode(plain_text):
    plain_text = plain_text.lower()
    answer = ""
    for i in plain_text:
        if i in plain:
            answer += cipher[plain.index(i)]
        elif i in numbers:
            answer += i 
    return spacing(answer)
            
def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    answer = ""
    for i in ciphered_text:
        if i in cipher:
            answer += plain[cipher.index(i)]
        elif i in numbers:
            answer += i  
    return answer

def spacing(phrase):
    fixed_answer = ""
    count = 0
    for letter in phrase:
        if count == 5:
            fixed_answer += " "
            fixed_answer += letter
            count = 1
        else:
            fixed_answer += letter
            count += 1
    return fixed_answer         