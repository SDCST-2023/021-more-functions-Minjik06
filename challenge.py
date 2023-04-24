#!python3

"""
Population growth can be modeled with the equation P = p*(1+r)^n
Where 
P is the future Population
p is the current population
r is the annual rate of grown as a decimal
n is the number of years

Write a function to determine the future population

Given 2 groups with given starting populations and different rates of growth,
determine how many years in the future they will have the same population or 
if they are diverging and will never have the same population
"""
import math
import time
def population(p,r,n):
    P=p*math.pow((1+r),n)
    print(round(P))
    return P

def equal(p1,r1,p2,r2):   
    try:
        n=1
        while True:
            n+=0.05
            pP1= p1*math.pow((1+r1),n)      
            pP2= p2*math.pow((1+r2),n) 
            if r1<r2 and p1<p2 or r1>r2 and p1>p2:
                print("None")
                return None
            else:
                if round(pP1)==round(pP2):
                    print(round(n))
                    return n
    except:
        return None
    

def tests():
    assert round(population(1000,.05, 5)) == 1276
    assert round(population(1000,.02, 20)) == 1486
    assert equal(1000,.05,2000,.06) == None
    assert round(equal(1000,.03,2000,.01)) == 35
tests()

 #math.log(1+r1,(1/p1))
    


"""try:
        while True:
            if round(pP1)==round(pP2):
                print(n)
                break
            elif round(pP1)!=round(pP2):
                n=n+1
        return n
    except:
        return None
        
        
        time.sleep(0.035)
        print(f"year:{n}, P1:{pP1}, P2:{pP2}")"""