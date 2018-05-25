class Account:
    def __init__(self,identification,balance = 0):
        self.balance = balance
        self.id = identification
    def addMoney(amount):
        self.balance = self.balance + money
    def getBalance():
        return self.balance
    def __str__(self):
        return"The balance of {} is {}".format(self.id,self.balance)

n = eval(input("How many accounts?"))
accountSet = set();
for i in range(n):
    string = input("Add the id and balance")
    string = string.split()
    accountSet.add(Account(eval(string[0]),eval(string[1])))

for x in accountSet:
    print(x)
        
