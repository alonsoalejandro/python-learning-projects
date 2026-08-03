def sum_of_multiples(limit, multiples):
    multiples_list = []
    total = 0
    for item in multiples:
        multiples_list.extend(calculate_multiples(item, limit))
    multiples_list = set(multiples_list)
    for i in multiples_list:
        total += i
    return total

def calculate_multiples(item, limit):
    return_multiples = []
    repetition = 1
    if item != 0:
        while item * repetition / limit < 1:
            return_multiples.append(item * repetition)
            repetition += 1
    else:
        return return_multiples
    return return_multiples