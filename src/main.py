from lib.player import Player
from lib.utils import shuffle, dealCards, generateDeck
from lib.cardGame import CardGame
import random

def main():
    
    startingPile = []   

    
    startingPile  = generateDeck()
    

    shuffledCards = shuffle(startingPile)
    
    for i in shuffledCards:
        print(" {0} ".format(i))
    print('\n')
    
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    dealCards(player1, player2, startingPile)
    print(player1.getDrawPile())
    print(player2.getDrawPile())
    
    game = CardGame()
    
    winner = None
    
    while True:
        winner = game.play(player1, player2)
        if(winner != None):
            break
    
    print(winner.getPlayerName() + " wins the game!")
    
if __name__ == "__main__":
    main()
   
   