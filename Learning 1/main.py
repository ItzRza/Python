import random
import time
import winsound

def random_num(a, b):
    global number
    number = random.randint(a, b)

def end_time():
    end = time.time()
    timer = end - start
    print(f"You guessed the number in {timer:.2f} seconds")
    print("================================================================")

def guess_num():
    try:
        guess = int(input("Guess number: "))
    except ValueError:
        print("Please enter a valid number!")
        winsound.Beep(300, 200)
        return guess_num()

    if guess > number:
        print("It's smaller")
        winsound.Beep(500, 300)
        guess_num()
    elif guess < number:
        print("It's bigger")
        winsound.Beep(500, 300)
        guess_num()
    else:
        print(f"It's true! Number was: {number}")
        winsound.Beep(1000, 500)
        end_time()

print("================================================================")

start = time.time()

while True:
    try:
        min_num = int(input("Min num: "))
        max_num = int(input("Max num: "))
        break
    except ValueError:
        print("Please enter valid numbers for range!")

random_num(min_num, max_num)

guess_num()
