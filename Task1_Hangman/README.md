# Hangman Word Guessing Game

## Description

Hangman is a console-based word guessing game developed using Python. The program randomly selects an English word, and the player tries to guess it one letter at a time before running out of attempts.

## Features

- Random English word selection
- Word list loaded from a text file
- Hidden letters displayed as underscores
- Letter-by-letter guessing
- ASCII hangman drawings
- Maximum of six incorrect guesses
- Duplicate guess detection
- Input validation
- Victory and defeat messages
- Option to play again

## Technologies Used

- Python 3
- `random` module
- Sets
- Functions
- File handling

## Project Files

- `hangman.py` — Main game program
- `google-10000-english-no-swears.txt` — English word list

## Requirements

- Python 3

No external Python libraries are required.

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the `Task1_Hangman` folder.
3. Run the following command:

```bash
python hangman.py
```

4. Enter one English letter when prompted.
5. Continue guessing until you win or use all six incorrect guesses.
6. Choose whether to play again.

## How It Works

The program selects a random word from the word list and hides its letters. Correct guesses reveal matching letters, while incorrect guesses advance the hangman drawing. Repeated guesses do not count as additional mistakes.

## Purpose

This project demonstrates basic Python programming concepts, including loops, conditions, sets, functions, random selection, file handling, and input validation.
