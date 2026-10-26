import random

def guessingGame():
    secretNum = random.randint(1, 1000)
    attempts = 0

    print("")
    print("Welcome to Secret Number!")
    print("------------------------------------\n")
    print("I'm thinking of a number between 1 and 1,000.\n")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secretNum:
            print("Too low! Try again.\n")
        elif guess > secretNum:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! You guessed the secret number in {attempts} attempts.\n")
            break


if __name__ == "__main__":

    guessingGame()
