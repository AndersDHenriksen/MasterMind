import itertools
import random
from game import compare_guess, n_pins


class Player:
    def __init__(self):
        pass

    def guess(self):
        pass

    def update_possible(self, guess, outcome):
        pass


class BruteForcePlayer:

    def __init__(self):
        self.possible_guess = list(itertools.product(range(1, 9), repeat=n_pins))

    def guess(self):
        return random.choice(self.possible_guess)

    def update_possible(self, guess, outcome):
        for i in reversed(range(len(self.possible_guess))):
            answer = self.possible_guess[i]
            if compare_guess(guess, answer) != outcome:
                self.possible_guess.pop(i)


class HumanPlayer(Player):

    def guess(self):
        guess = ''
        while len(guess) != 5:
            guess = input("Guess: ")
            guess = guess.replace(" ", "")
        print("")
        return [int(i) for i in guess]
