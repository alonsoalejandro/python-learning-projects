def square_root(number):
    #Applying binary search
    min_value = 1
    max_value = number
    mid_value = (min_value + max_value) // 2
    while mid_value * mid_value != number:
        if mid_value * mid_value > number:
            max_value = mid_value - 1
        elif mid_value * mid_value < number:
            min_value = mid_value + 1
        mid_value = (min_value + max_value) // 2
    return mid_value