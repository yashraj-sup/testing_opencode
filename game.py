import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_guess():
    while True:
        raw = input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): ")
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            continue
        return guess


def play_round():
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses = 0

    while True:
        guess = get_guess()
        guesses += 1
        if guess < secret:
            print("Too low! Try a higher number.")
        elif guess > secret:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! You guessed it in {guesses} guess" + ("es." if guesses != 1 else "."))
            return


def main():
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
