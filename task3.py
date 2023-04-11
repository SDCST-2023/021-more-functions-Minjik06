#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse rounded to 2 decimals
        None if the hypotenuse does not exist

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
import math

def hypotenuse(a,b):
    try:
        a=float(a)
        b=float(b)
        c = math.sqrt(math.pow(a,2)+math.pow(b,2))
        print(round(c, 2))
        return round(c, 2)
    except:
        print("None")
        return None
try:
    assert hypotenuse(6,8) == 10
    assert hypotenuse(5,12) == 13
    assert hypotenuse(4,6) == 7.21
    assert hypotenuse(-3,4) == 5
except:
    print("Wrong")