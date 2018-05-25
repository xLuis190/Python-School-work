#Luis Felipe Jimenez Ferreira
#Program #1
'''
def countOdd(Dictionary):
    oddCounter = 0
    for x in Dictionary:
        if(Dictionary[x] %2 == 1):
            oddCounter = oddCounter +1
    print(oddCounter)

D = {1:3,'a':5,'z':8}
countOdd(D)
'''
#Program #2
'''
class Clock:
    def __init__(self,time):
        self.time = time

    def addTime(self,t):
        self.time = self.time + t
        while(self.time >= 24):
            self.time =  self.time - 24
            
    def getTime(self):
        return self.time

C = Clock(22)
print(C.getTime())
print("------")
C.addTime(5)
print(C.getTime())
print("------")
C.addTime(50)
print(C.getTime())
'''
#Program #3

class Stg:
    def __init__(self):
        self.S = []
    def add(self,string):
        self.S.append(string)
    def get(self,index):
        if(index < len(self.S)):
            return self.S[index]
        else:
            return "Out of bounds"
    
    def change(self,singleChar,n):
        if n < len(self.S):
           self.S[n] = singleChar
        else:
            return"Out of bounds"

S = Stg()
S.add('a')
S.add('b')
S.add('c')
print(S.get(0))
print(S.get(8))
S.change('x',0)
S.change('y',7)
print(S.get(0))
print(S.get(7))

#Problem #4
'''
class Bit:
    def __init__(self, v = 0):
        self.v = v

    def flip(self):
        self.v = (self.v +1) %2
    def __str__(self):
        return str(self.v)

def printBitList(L):
    for x in L:
        print(x,end="")
    print("")
def flipBits(L):
    for x in L:
        x.flip()
        

L = [Bit(1), Bit(0), Bit()]
printBitList(L)
flipBits(L)
printBitList(L)
'''
#Problem #5
'''
count = 0
L = []
while True:
    if(count >= 100):
        break;
    num = eval(input("Please give me some numbers "))
    count = num + count;
    L.append(num)
print(max(L))
'''





