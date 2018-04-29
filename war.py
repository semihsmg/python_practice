from random import shuffle


class Card:
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    def __init__(self, value, suit):
        # suits and values should be integers
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] + ' of ' + self.suits[self.suit]


# hand1 = Card(5, 1)
# hand2 = Card(3, 3)
# print(hand1)
# print(hand2)
# print(hand1 < hand2)


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# deck = Deck()
# for card in deck.cards:
#     print(card)

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('P1: ')
        name2 = input('P2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print('Beginning War!')
        response = None
        while len(cards) >= 2 and response != 'q':
            response = input('Press any key to play.\n'
                             'q to quit\n'
                             '-------------------------')
            if response == 'q':
                break
            p1_card = self.deck.remove_card()
            p2_card = self.deck.remove_card()
            print('{} drew {}\n{} drew {}'.format(self.p1.name, p1_card, self.p2.name, p2_card))
            if p1_card > p2_card:
                self.p1.wins += 1
                print('{} wins this round'.format(self.p1.name))
            else:
                self.p2.wins += 1
                print('{} wins this round'.format(self.p2.name))
        print('The War is over.\n'
              'Score: {} {}\n'
              '{} wins...'.format(self.p1.wins, self.p2.wins, self.winner(self.p1, self.p2)))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'It was a tie!'


game = Game()
game.play_game()
