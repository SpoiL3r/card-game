
from utils import generateDeck, shuffle
import random
import unittest

class TestShuffle(unittest.TestCase):
    
    def testCheckSize(self):
        
        """deck size should contain 40 cards"""
        startingPile = []
        startingPile  = generateDeck()
        
        self.assertEqual(len(startingPile), 40)
    
    
    def testShuffle(self):
        """shuffle should shuffle a deck"""
        startingPile = generateDeck()
        self.assertEqual(startingPile, shuffle(startingPile))
    
