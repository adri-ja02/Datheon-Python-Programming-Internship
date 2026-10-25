
import random

# Name of the downloaded English word list
WORD_FILE = "google-10000-english-no-swears.txt"

# Maximum number of incorrect guesses
MAX_ATTEMPTS = 6


# ASCII art for each stage of the Hangman game
HANGMAN_ART = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]


def load_words():
    """Load English words from the provided text file."""
    try:
        with open(WORD_FILE, "r", encoding="utf-8") as file:
            words = [
                line.strip().lower()
                for line in file
                if line.strip().isalpha()
                and line.strip().isascii()
                and 4 <= len(line.strip()) <= 10
            ]

        if not words:
            print("Error: The word list is empty.")
            raise SystemExit(1)

        return words

    except FileNotFoundError:
        print(f"Error: '{WORD_FILE}' was not found.")
        print("Please place the word list in the same folder as hangman.py.")
        raise SystemExit(1)


def display_word(secret_word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game(words):
    """Run one round of the Hangman game."""

    # Select a random secret word
    secret_word = random.choice(words)

    # Sets store letters without duplicates
    guessed_letters = set()
    correct_letters = set()
    incorrect_letters = set()

    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("       WELCOME TO HANGMAN!")
    print("=" * 40)
    print(f"\nYour secret word has {len(secret_word)} letters.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses available.")

    # Continue until the player wins or runs out of attempts
    while wrong_guesses < MAX_ATTEMPTS:

        # Display the current gallows stage
        print(HANGMAN_ART[wrong_guesses])

        # Display the masked word
        print("Word:", display_word(secret_word, guessed_letters))

        # Display guessed letters
        print("Correct letters:",
              " ".join(sorted(correct_letters)) or "None")
        print("Incorrect letters:",
              " ".join(sorted(incorrect_letters)) or "None")

        print(f"Attempts remaining: {MAX_ATTEMPTS - wrong_guesses}")

        # Ask the player for one letter
        guess = input("\nGuess a letter: ").strip().lower()

        # Validate the input
        if (
            len(guess) != 1
            or not guess.isalpha()
            or not guess.isascii()
        ):
            print("Invalid input! Please enter one English letter (A-Z).")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Record the new guess
        guessed_letters.add(guess)

        # Check whether the letter is in the secret word
        if guess in secret_word:
            correct_letters.add(guess)
            print(f"Correct! '{guess}' is in the word.")

            # Check whether the entire word has been guessed
            if all(letter in guessed_letters for letter in secret_word):
                print(HANGMAN_ART[wrong_guesses])
                print("Word:", display_word(secret_word, guessed_letters))
                print("\nCONGRATULATIONS! YOU WON!")
                print(f"The secret word was: {secret_word}")
                return

        else:
            incorrect_letters.add(guess)
            wrong_guesses += 1

            print(f"Incorrect! '{guess}' is not in the word.")

    # Display the final gallows after six incorrect guesses
    print(HANGMAN_ART[MAX_ATTEMPTS])
    print("\nGAME OVER! YOU LOST.")
    print(f"The correct word was: {secret_word}")


def main():
    """Load the word list and allow repeated games."""

    words = load_words()

    while True:
        play_game(words)

        play_again = input(
            "\nWould you like to play again? (y/n): "
        ).strip().lower()

        if play_again != "y":
            print("\nThank you for playing Hangman. Goodbye!")
            break


# Start the program
if __name__ == "__main__":
    main()
