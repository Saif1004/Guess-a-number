import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number: "))
        if guess> random_number:
            print(f"Sorry {guess} is too high. Try again.")
        elif guess< random_number:
            print(f"Sorry {guess} is too low")

    print(f"{guess} is correct")

guess(100)




