
import unittest
from player import Player
from cardGame import CardGame

class TestPlayerDrawCard(unittest.TestCase):

    def testDrawCardFromEmptyDrawPile(self):
        """ If a player with an empty draw pile tries to draw a card, the discard pile is shuffled into the draw pile."""
        testPlayer = Player('test')
        testPlayer.addCardToDiscardPile(10)
        testPlayer.addCardToDiscardPile(7)
        testPlayer.addCardToDiscardPile(8)
        testPlayer.addCardToDiscardPile(3)
        
        testPlayer.drawCard()
        
        self.assertEqual(3, len(testPlayer.getDrawPile()))
    
    def testHigherCardShouldWin(self):
        """ When comparing two cards, the higher card should win."""
        player1 = Player("Player 1");
        player2 = Player("Player 2");

        player1.addToDrawPile(1);
        player1.addToDrawPile(2);
        player1.addToDrawPile(3);

        player2.addToDrawPile(4);
        player2.addToDrawPile(5);
        player2.addToDrawPile(6);

        game = CardGame()
        game.play(player1,player2);

        self.assertTrue(player2.getNumberOfCards() > player1.getNumberOfCards());
        
    def testEqualCards(self):
        """When comparing two cards of the same value, the winner of the next round should win 4 cards."""
        
        player1 = Player("Player 1");
        player2 = Player("Player 2");
        
        player1.addToDrawPile(1);
        player1.addToDrawPile(2);
        player1.addToDrawPile(3);

        player2.addToDrawPile(1);
        player2.addToDrawPile(6);
        player2.addToDrawPile(6);

        game = CardGame()
        game.play(player1,player2);
        game.play(player1,player2);

        self.assertTrue(player2.getNumberOfCards() - player1.getNumberOfCards() == 4);

