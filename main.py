import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#Card Class

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank +  ' of '+ self.suit


class Deck:

    def __init__(self):
        self.deck = [] #empty List
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) #build Card objects and them to the list

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' +card.__str__() # collect collection of card from __init__ function
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace' :
            self.aces += 1


    def adjust_card(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self,total):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("how many chips would you like to bet? "))
        except:
            print("sorry plz Enter A valid number")
        else:
            if chips.bet > chips.total:
                print('Sorry, You do not have enough chips! You have : {}'.format(chips.total))
            else:
                break

if __name__ == '__main__':

    test_deck = Deck()
    test_deck.shuffle()

    test_player = Hand()
    #print(test_deck.deal())
    test_player.add_card(test_deck.deal())
    test_player.add_card(test_deck.deal())
    test_player.value