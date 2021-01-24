class CardGame:
    def __init__(self):
        self.equalCardsPile = []
        
    def play(self, player1, player2):
        player1Output = 'Player 1 ( {0} cards ): '.format(player1.getNumberOfCards())
        playerOneCard = player1.drawCard()
        
        if(playerOneCard == -1):
            return player2
        
        player2Output = 'Player 2 ( {0} cards ): '.format(player2.getNumberOfCards())
        playerTwoCard = player2.drawCard()
        
        if(playerTwoCard == -1):
            return player1
        
        print(player1Output + str(playerOneCard))
        print(player2Output + str(playerTwoCard))
        
        if(playerOneCard > playerTwoCard):
            print("Player 1 wins the round")
            print("\n")
            player1.addCardToDiscardPile(playerOneCard)
            player1.addCardToDiscardPile(playerTwoCard)
            player1.addEqualCardsToDiscardPile(self.equalCardsPile)
            self.equalCardsPile = []
            
        elif(playerTwoCard > playerOneCard):
            print("Player 2 wins the round")
            print("\n")
            player2.addCardToDiscardPile(playerOneCard)
            player2.addCardToDiscardPile(playerTwoCard)
            player2.addEqualCardsToDiscardPile(self.equalCardsPile)
            self.equalCardsPile = []
        
        else:
            print("No winner in this round")
            print("\n")
            self.equalCardsPile.append(playerOneCard)
            self.equalCardsPile.append(playerTwoCard)
            
        return None