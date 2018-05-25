#F(x) = x^2 + 10x + 25
import math

def F(x):
    result =math.pow(x,3)+ (3*math.pow(x,2)) + (10*x)
    return math.floor(result)



print("F(x) = x^3 +3x^2 + 10x")
for x in range(-55,55):
    print("({},{})".format(x,F(x)))
