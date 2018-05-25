import random
class Dice:
    def __init__(self,n = 6):
        self.n = n;
        self.dies1 = 6;
        self.dies2 = 6;
    def roll(self):
        self.R1 = random.randint(0,dies1)
        self.R2 = random.randInt(0,dies2)
        return self.R1 + self.R2;
    def state(self):
        print("({},{})".format(self.R1 , self.R2)));
    def rollrepeat(self,x,t):
        sumatory = 0;
        roll = 0;
        for x in range(t):
            roll = self.roll()
            if(roll == x):
                sumatory = sumatory +1;
        return sumatory;
        
    def __str__(self):
        return self.state();
        
