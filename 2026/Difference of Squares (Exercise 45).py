def square_of_sum(number):
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += i
    return total_sum ** 2

def sum_of_squares(number):
    sum_squares = 0
    for i in range(1, number + 1):
        sum_squares += i ** 2
    return sum_squares

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)