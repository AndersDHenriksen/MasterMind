import random

n_pins = 5
n_guess = 10

master_answer = [str(random.randint(1, 8)) for i in range(n_pins)]
# print(master_answer)


def print_row(array, correct_count):
    char_array = " ".join(str(a) for a in array)
    pin_array = correct_count[0] * "○" + correct_count[1] * "●" + (len(array) - sum(correct_count)) * " "
    print(f"│ {char_array} │ {pin_array} │")


def print_line(type):
    ends = {"start": "┌┐", "middle": "├┤", "end": "└┘"}
    middle = {"start": "┬", "middle": "┼", "end": "┴"}
    assert type in ends.keys()
    middle_segment = 11 * "─" + middle[type] + 7 * "─"
    print(str(middle_segment).join(ends[type]))


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


def compare_guess(guess):
    guess = list(guess)
    answer = master_answer.copy()
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
    guesses, answers = [], []
    fully_correct_guess = False
    while not (fully_correct_guess or len(guesses) >= 10):
        guess = ''
        while len(guess) != 5:
            guess = input("Guess: ")
            guess = guess.replace(" ", "")
        print("")
        guesses.append(guess)
        answers.append(compare_guess(guess))
        fully_correct_guess = answers[-1][0] == 5
        print_board(guesses, answers, fully_correct_guess)
    if fully_correct_guess:
        print("Congrats!")
    else:
        print(f"Failure! Answer was: {master_answer}")


if __name__ == '__main__':
    game_loop()

