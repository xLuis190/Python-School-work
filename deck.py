from random import *
class BlackJack:
    def
class Deck:
    def __init__(self):
        cardtypes = ['spades','hearts','diamond','clubs']
        self.deck = []
        for x in cardtypes:
            for number in range(1,13):
                self.deck.append((x,number))
        self.shuffle()
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
        print(randCard)
        self._remove(randCard[0],randCard[1])
        return self.deck[x]

    def _remove(self,cardType,number):
        self.deck.remove((cardType,number))
        

D = Deck()
D.getRandomCard()
print(D.getDeck())
