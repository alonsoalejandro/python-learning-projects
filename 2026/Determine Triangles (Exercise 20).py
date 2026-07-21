def is_valid_triangle(sides):
    #Verify the triangle
    a, b, c = sides
    return (
        a > 0
        and b > 0
        and c > 0
        and a + b >= c
        and a + c >= b
        and b + c >= a
    )

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2] #Same length

def isosceles(sides):
    #At least two equal sides
    if not is_valid_triangle(sides):
        return False
    return (
        sides[0] == sides[1]
        or sides[0] == sides[2]
        or sides[1] == sides[2]
    )

def scalene(sides):
    #Different lenght each triangle
    if not is_valid_triangle(sides):
        return False
    return (
        sides[0] != sides[1]
        and sides[0] != sides[2]
        and sides[1] != sides[2]
    )