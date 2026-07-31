def line_up(name, number):
    position = "th"
    number = str(number)
    if number[-1] == "1":
        if len(number) == 1 or number[-2:] != "11":
            position = "st"
    elif number[-1] == "2":
        if len(number) == 1 or number[-2:] != "12":
            position = "nd"
    elif number[-1] == "3":
        if len(number) == 1 or number[-2:] != "13":
            position = "rd"
    return name + ", " + "you are the " + str(number) + position + " customer we serve today. Thank you!"