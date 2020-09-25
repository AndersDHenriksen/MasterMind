import random
import bot

n_pins = 5
n_guess = 10

use_bot = True

master_answer = [random.randint(1, 8) for _ in range(n_pins)]
# print(master_answer)


def strl(int_list):
    return " ".join(str(i) for i in int_list)


def print_row(array, correct_count):
    char_array = " ".join(str(a) for a in array)
    pin_array = correct_count[0] * "○" + correct_count[1] * "●" + (len(array) - sum(correct_count)) * " "
    print(f"│ {char_array} │ {pin_array} │")


def print_line(kind):
    ends = {"start": "┌┐", "middle": "├┤", "end": "└┘"}
    middle = {"start": "┬", "middle": "┼", "end": "┴"}
    assert kind in ends.keys()
    middle_segment = 11 * "─" + middle[kind] + 7 * "─"
    print(str(middle_segment).join(ends[kind]))


def print_board(guesses, answers, reveal=False):
    print_line("start")
    guess_left = n_guess - len(guesses)
    guesses_print = guesses + guess_left * [n_pins * "."]
    answers_print = answers + guess_left * [(0, 0)]
    for guess, answer in zip(guesses_print, answers_print):
        print_row(guess, answer)
        print_line("middle")
    print_row("XXXXX" if not reveal else master_answer, (0, 0))
    print_line("end")


def compare_guess(guess, answer=None):
    answer = master_answer.copy() if answer is None else list(answer)
    guess = list(guess)
    n_correct, n_present = 0, 0
    for i in reversed(range(n_pins)):
        if guess[i] == answer[i]:
            n_correct += 1
            guess.pop(i)
            answer.pop(i)
    for i in reversed(range(len(guess))):
        if guess[i] in answer:
            n_present += 1
            answer.pop(answer.index(guess[i]))
            guess.pop(i)
    return n_correct, n_present


def game_loop():
    player = bot.BruteForcePlayer() if use_bot else bot.HumanPlayer()
    guesses, answers = [], []
    fully_correct_guess = False
    while not (fully_correct_guess or len(guesses) >= n_guess):
        guess = player.guess()
        guesses.append(guess)
        answers.append(compare_guess(guess))
        fully_correct_guess = answers[-1][0] == n_pins
        print_board(guesses, answers, fully_correct_guess)
        player.update_possible(guess, answers[-1])
    if fully_correct_guess:
        print(f"\nCongrats, you won in {len(guesses)} guesses!")
    else:
        print(f"\nFailure! Answer was: {strl(master_answer)}")
    return len(guesses)


if __name__ == '__main__':
    # needed_guesses = 100 * [None]
    # for i in range(100):
    #     needed_guesses[i] = game_loop()
    # print(f"Average number of guesses required: {sum(needed_guesses)/len(needed_guesses)}")
    game_loop()

