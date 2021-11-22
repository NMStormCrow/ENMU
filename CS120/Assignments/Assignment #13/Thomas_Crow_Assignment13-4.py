#   Assignment #13 Question #4
#
#   Thomas Crow
#   Date 11/20/2021
#
#   Requirements: Implement a class to represent a playing card. Your class should have the following 
#                 methods:
#                 __init__(self, rank, suit) rank is an int in the range 1-13 indicating the ranks ace-king and
#                 suit is a single character "d" "c" "h" or "s" indicating the suit (diamonds, clubs.
#                 hearts, or spades). Create the corresponding card.
#                 getRank(self) Returns the rank of the card
#                 getSuit(self) Returns the suit of the card
#                 value(self) Returns the Blackjack value of the card. Ace counts as 1, face cards count as 10
#                 __str__(self) Returns a string than names the card. For example, "Ace of Spades"
#                 Note: A method named str is special in Python. If asked to convert an object into a 
#                 string, Python uses this method, if it's present. For example,
#                 c = Card(1,"s")
#                 print c
#                 will print "Ace of Spades"
#                 Test you card class with a program that prints out n randomly generated cards and the 
#                 associated Blackjack balue where n is a number supplied by the user

import random

class PlayingCard:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if (self.rank >= 10):
            return 10
        else:
            return self.rank
    
    def __str__(self):
        rankList = ["Empty","Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        suitList = {'c': 'Clubs', 'd': 'Diamonds', 'h': 'Hearts', 's': 'Spades'}
        return rankList[self.rank] + ' of ' + suitList[self.suit]


def main():

    suitList = ['c','d','h','s']
    print("This program will print out n-number of playing cards.")
    userN = eval(input("Please enter the value for n: "))
    for i in range(userN):
        rank = (random.randrange(1,13))
        suit = (random.choice(suitList))
        card = PlayingCard(rank, suit)
        print(f"Card number {(i+1)} is the {card}. Its blackjack value is {card.value()}")
    


if __name__ == '__main__':
    main()
