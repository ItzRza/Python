import time
import random
import winsound
import os


def get_separator_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 60


def input_num():
    global min_num
    global max_num
    min_num = int(input("Min num: "))
    max_num = int(input("Max num: "))


def random_num(a, b):
    global number
    number = random.randint(a, b)


def time_start():
    global start_time
    start_time = time.time()


def time_end():
    global end_time
    end_time = time.time()


def time_timer():
    return end_time - start_time


def guess_num():
    width = get_separator_width()
    print("=" * width)
    while True:
        try:
            guess = int(input("Guess number: "))
        except ValueError:
            print("Please enter a valid number!")
            winsound.Beep(500, 200)
            continue

        if guess > number:
            print("It's smaller")
            winsound.Beep(500, 100)
        elif guess < number:
            print("It's bigger")
            winsound.Beep(500, 500)
        else:
            print(f"It's true! Number was: {number}")
            winsound.Beep(1000, 500)
            time_end()
            print(f"You guessed the number in {time_timer():.2f} seconds")
            print("=" * width)
            break


def run_game():
    input_num()
    random_num(min_num, max_num)
    time_start()
    guess_num()


run_game()
