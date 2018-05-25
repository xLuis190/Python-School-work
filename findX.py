import math
def findValues(L):
    x1 = math.floor((-L[1] + math.sqrt(math.pow(L[1],3) - 4*(L[0]*(L[2])))) / 2*L[0])
    x2 = math.floor((-L[1] - math.sqrt(math.pow(L[1],3) - 4*(L[0]*(L[2]))))/ 2*L[0])
    print((x1,x2))

findValues([1,10,25])
