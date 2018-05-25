'''
james stefanik (james.stefanik@gmail.com)
'''

from random import *
class BlackJack:

    def __init__(self):
        self.User = User()
        self.deck = Deck()
        
    def play(self):
        self.User.printIntro()
        self.hand = []
        for x in range(1,3):
            self.hand.append(self.deck.getRandomCard())
        print(self.hand)
        self.User.printHand(self.hand)
        s = self.User.stayOrHit()
        
        if( s == "hit"):
             self.hand.append(self.deck.getRandomCard())
             self.User.printHand(self.hand)
             self.User.stayOrHit()
        else:
            self.User.getRoundTotal()
            self.User.getFinalTotal()
            self.User.wipe()
        boolean = self.User.continuePlaying()
        if(boolean):
            self.play()
        else:
            print("Get the fuck out of here")
            self.User.getFinalTotal();

class User:
    def __init__(self):
        self.round_total = 0
        self.final_total = 0
        
    def wipe(self):
        self.round_total = 0;
    def printIntro(self):
        print("Welcome to Blackjack")
        
    def continuePlaying(self):
        userInput = input(" Countinue play or end game?[yes or no]: ")
        userInput.lower()
        userInput.split()
        return userInput[0] == 'y'
    
    def printHand(self,L):
        for cardType,number in L:
            self.round_total = self.round_total + number;
        print("Your hand is {} and your Round total is {}".format(L,self.round_total))
            
        
    def anotherCard():
        userInput = input("Do you want another card (yes or no)")
        userInput.lower()
        userInput = userInput.split()
        return userInput[0] == y;
    
    def stayOrHit(self):
        userInput = input("Do you stay or hit?: ")
        if(userInput == "stay"):
            return "stay"
        if(userInput == "hit"):
            return "hit"
    def getRoundTotal(self):
        print("Round Score:", self.round_total)
    def getFinalTotal(self):
        if(13 < self.round_total < 21):
            self.final_total += self.round_total
            print("Total Score:",self.final_total)
            
class Deck:
    def __init__(self):
        cardtypes = ['spades','hearts','diamond','clubs']
        self.deck = []
        for x in cardtypes:
            for number in range(1,13):
                self.deck.append((x,number))
        shuffle(self.deck)
    def printDeck(self):
        print(self.deck)
        
    def getDeck(self):
        return self.deck
    def shuffle(self):
        shuffle(self.deck)
    def _remove(self,cardType,number):
        self.deck.remove((cardType,number))
    def getRandomCard(self):
        x = randint(1,13)
        randCard = self.deck[x]
        self._remove(randCard[0],randCard[1])
        return self.deck[x]

    def _remove(self,cardType,number):
        self.deck.remove((cardType,number))
        


def main():
    BJ = BlackJack()
    BJ.play()
main()
