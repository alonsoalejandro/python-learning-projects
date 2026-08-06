alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet.upper()
def rows(letter):
    diamond = []
    index = alphabet.index(letter)
    width = index * 2 + 1
    # Parte superior
    for i in range(index + 1):
        current = alphabet[i]
        left = index - i
        if i == 0:
            row = " " * left + "A" + " " * left
        else:
            inside = 2 * i - 1
            row = (
                " " * left
                + current
                + " " * inside
                + current
                + " " * left
            )
        diamond.append(row)
    # Parte inferior
    for i in range(index - 1, -1, -1):
        current = alphabet[i]
        left = index - i
        if i == 0:
            row = " " * left + "A" + " " * left
        else:
            inside = 2 * i - 1
            row = (
                " " * left
                + current
                + " " * inside
                + current
                + " " * left
            )
        diamond.append(row)
    return diamond