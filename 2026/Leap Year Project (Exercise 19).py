def leap_year(year):
    #Verify the conditions given for leap years, I suppose the parameter year is an int
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
    
    


    
