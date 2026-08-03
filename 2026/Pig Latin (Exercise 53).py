VOWELS = "aeiou"

def translate(text):
    translated = []

    for word in text.split():
        # Rule 1
        if word[0] in VOWELS or word.startswith(("xr", "yt")):
            translated.append(word + "ay")
            continue
        i = 0
        # Rule 3
        while True:
            if word[i:i + 2] == "qu":
                i += 2
                break
            # Rule 4
            if word[i] == "y" and i != 0:
                break
            # Rule 2
            if word[i] in VOWELS:
                break
            i += 1
        translated.append(word[i:] + word[:i] + "ay")
    return " ".join(translated)