def find(search_list, value): 
    highest_value_index = len(search_list) - 1
    lowest_value_index = 0

    while lowest_value_index <= highest_value_index:
        mid = (lowest_value_index + highest_value_index)//2
        guess = search_list[mid]
        if guess == value:
            return mid
        if guess > value:
            highest_value_index = mid -1
        if guess < value:
            lowest_value_index = mid + 1
    raise ValueError("value not in array")