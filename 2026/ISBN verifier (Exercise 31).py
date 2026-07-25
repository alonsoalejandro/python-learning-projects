def is_valid(isbn):
    amount = 0 #the sum of all values
    repetition = 10 #the amount of cicles needed to complete in for loop
    complete_isbn = isbn.replace("-", "")
    
    if len(complete_isbn) != 10:
        return False
    
    last_position = complete_isbn[-1] == "X" or complete_isbn[-1].isdigit()
    
    if complete_isbn[:-1].isdigit() and last_position:
        for i in complete_isbn:
            if repetition > 1:
                amount += int(i)*repetition
                repetition -= 1
            else:
                if i == "X":
                    amount += 10*repetition
                else:
                    amount += int(i)*repetition
        return amount % 11 == 0   
    else:
        return False