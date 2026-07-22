def is_armstrong_number(number):
    #Transform it into a list
    digits = list(str(number))
    amount = 0
    for i in digits:
        amount += int(i) ** len(digits)
    if amount == number:
        return True
    return False