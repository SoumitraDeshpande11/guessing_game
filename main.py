import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while not guessed:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()

