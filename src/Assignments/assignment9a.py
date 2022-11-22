#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignment #9a
#Date Created: 11/22/2022
#Date Modified: 11/22/2022
#############################################################################

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
                "Ace",
            ]:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()
deck.shuffle()
card1 = deck.cards.pop()
print(card1)
