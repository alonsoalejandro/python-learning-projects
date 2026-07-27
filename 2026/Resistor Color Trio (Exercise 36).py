dict_colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def label(colors):
    first_two = str(dict_colors[colors[0]]) + str(dict_colors[colors[1]])
    number_zeros = int(dict_colors[colors[2]])
    answer = first_two + (number_zeros * "0")
    answer = int(answer)
    if answer != 0:
        if answer % (10**9) == 0:
            return str(answer//(10**9)) + " gigaohms"
        elif answer % (10**6) == 0:
            return str(answer//(10**6)) + " megaohms"
        elif answer % (10**3) == 0:
            return str(answer//(10**3)) + " kiloohms"
        else:
            return str(answer) + " ohms"
    else:
        return "0 ohms"
            