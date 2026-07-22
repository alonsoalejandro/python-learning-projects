number_in_square = int(1)
total_amount = int(0)

def square(number):
    number_in_square = int(1)
    if 1 <= number <= 64:
        for i in range(number-1):
            if i == 0:
                number_in_square = int(1)
            number_in_square *= 2
        return number_in_square                
    else:
        raise ValueError("square must be between 1 and 64")
        
def total():
    number_in_square = 1
    total_amount = 0
    for i in range(64):
        total_amount += number_in_square
        number_in_square *= 2
    return total_amount