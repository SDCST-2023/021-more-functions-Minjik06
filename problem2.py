#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math
def triangle(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=max(a,b,c)
    if d==a:
        if math.pow(d,2)<math.pow(b,2)+math.pow(c,2):
            if d>b+c:
                print("0 : triangle does not exist")
                return 0
            print("1 : triangle is acute")
            return 1
        elif math.pow(d,2)==math.pow(b,2)+math.pow(c,2):
            if d>b+c:
                print("0 : triangle does not exist")
                return 0
            print("2 : triangle is right")
            return 2
        else:
            if d>b+c:
                print("0 : triangle does not exist")
                return 0
            elif math.pow(d,2)>math.pow(b,2)+math.pow(c,2):
                print("3 : triangle is obtuse")
                return 3
    elif d==b:
        if math.pow(d,2)<math.pow(a,2)+math.pow(c,2):
            if d>c+a:
                print("0 : triangle does not exist")
                return 0
            print("1 : triangle is acute")
            return 1
        elif math.pow(d,2)==math.pow(a,2)+math.pow(c,2):
            if d>c+a:
                print("0 : triangle does not exist")
                return 0
            print("2 : triangle is right")
            return 2
        else:
            if d>c+a:
                print("0 : triangle does not exist")
                return 0
            elif math.pow(d,2)>math.pow(c,2)+math.pow(a,2):
                print("3 : triangle is obtuse")
                return 3
    elif d==c:
        if math.pow(d,2)<math.pow(b,2)+math.pow(a,2):
            if d>b+a:
                print("0 : triangle does not exist")
                return 0
            print("1 : triangle is acute")
            return 1
        elif math.pow(d,2)==math.pow(b,2)+math.pow(a,2):
            if d>b+a:
                print("0 : triangle does not exist")
                return 0
            print("2 : triangle is right")
            return 2
        else:
            if d>b+a:
                print("0 : triangle does not exist")
                return 0
            elif math.pow(d,2)>math.pow(b,2)+math.pow(a,2):
                print("3 : triangle is obtuse")
                return 3

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()

def main():
    a=float(input("one side"))
    b=float(input("another side"))
    c=float(input("3rd side"))
    triangle(a,b,c)
main()
