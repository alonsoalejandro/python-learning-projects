def classify(number):
    factors_list = []
    if number >= 1:
        for i in range(1, number):
            if number % i == 0:
                factors_list.append(i)
        factors_sum = sum(factors_list)
        if factors_sum == number:
            return "perfect"
        elif factors_sum > number:
            return "abundant"
        elif factors_sum < number:
            return "deficient"
    else:
        raise ValueError("Classification is only possible for positive integers.")