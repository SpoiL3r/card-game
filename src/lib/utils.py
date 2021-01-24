import random

def generateDeck():
    startingPile = []
    for i in range(1,11):
        startingPile.append(i)
        startingPile.append(i)
        startingPile.append(i)
        startingPile.append(i)
        
    for i in startingPile:
        print(" {0} ".format(i))
            
    return startingPile
    


def shuffle(cards):
    if (len(cards) < 2):
        return cards
    #fischer-yates shuffling
    for i in range(len(cards)-1, 0,-1):
        j = random.randint(0,i)
        temp = cards[i]
        cards[i] = cards[j]
        cards[j] = temp
          
    return cards

def dealCards(player1, player2, shuffledPile):
    count = 0
    for i in range(len(shuffledPile)):
        if(count % 2 == 0):
            player1.addToDrawPile(shuffledPile[i])
        else:
            player2.addToDrawPile(shuffledPile[i])
            
        count += 1