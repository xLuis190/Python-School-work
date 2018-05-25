#Umar Ali
#Jeffrey Almanzar
#Luis Felipe Jimenez

def recFib(n):
    if n ==2:
        return 2
    if n == 1:
        return 1
    else:
       return recFib(n-2) + recFib(n-1)

def itterativeFib(n):
    a = 1
    b = 2
    for x in range(2,n):
        a,b = b, a+b
        
    return b
        


print("Itterative way: "+str(itterativeFib(9)))
print("Recursive way: "+str(recFib(9)))
