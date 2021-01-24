from utils import shuffle
class Player:
    def __init__(self, name):
        self.name = name
        self.drawPile = []
        self.discardPile = []
        
    def addToDrawPile(self,card):
        self.drawPile.append(card)
        
    
    def addCardToDiscardPile(self, card):
        self.discardPile.append(card)
        
        
    def addEqualCardsToDiscardPile(self, equalCardsPile):
        self.discardPile.extend(equalCardsPile)
    
    
    def drawCard(self):
        if (len(self.drawPile) > 0):
            return self.drawPile.pop(0)
        if (len(self.discardPile) > 0):
            shuffle(self.discardPile)
            self.drawPile.extend(self.discardPile)
            self.discardPile = []
            return self.drawCard()
        return -1
    
    
    def getNumberOfCards(self):
        return len(self.drawPile) + len(self.discardPile)
    
    
    def getPlayerName(self):
        return self.name
    
    def getDrawPile(self):
        return self.drawPile
    
    