import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_GUESSES = 5
CLOSE_GAP = 10


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

    for guesses in range(1, MAX_GUESSES + 1):
        guess = get_guess()
        remaining = MAX_GUESSES - guesses
        if guess < secret:
            if secret - guess > CLOSE_GAP:
                print("Too low! Try a higher number.")
            else:
                print("Low! Pick a higher number.")
        elif guess > secret:
            if guess - secret > CLOSE_GAP:
                print("Too high! Try a lower number.")
            else:
                print("High! Pick a lower number.")
        else:
            print(f"Correct! You guessed it in {guesses} guess" + ("es." if guesses != 1 else "."))
            return

        if remaining:
            print(f"{remaining} guess" + ("es" if remaining != 1 else "") + " left.")
        else:
            print(f"Out of guesses! The number was {secret}.")


def main():
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
