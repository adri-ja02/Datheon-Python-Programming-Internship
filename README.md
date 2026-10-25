# Datheon Python Programming Internship

Python programming projects completed during the Datheon Python Programming Internship.

This repository contains Python projects developed to practice programming fundamentals, file handling, data processing, input validation, and calculations.

## Tasks

### Task 1: Hangman Word Guessing Game

A console-based word guessing game developed using Python.

**Features**
- Random English word selection
- Word list loaded from a text file
- Letter-by-letter guessing
- ASCII hangman drawings
- Maximum of six incorrect guesses
- Input validation and duplicate guess detection
- Victory and defeat messages
- Replay option

**Technologies:** Python 3, random module, sets, functions, and file handling.

**How to run**

Open a terminal in the project directory and execute:

```bash
cd Task1_Hangman
python hangman.py
```

Ensure that `google-10000-english-no-swears.txt` is in the same folder as `hangman.py`.

### Task 2: Stock Portfolio Performance Tracker

A Python command-line application that tracks stock investments, calculates portfolio performance, and exports results to a CSV file.

**Features**
- Loads S&P 500 company symbols from `constituents.csv`
- Validates stock ticker symbols
- Accepts purchase prices and share quantities
- Retrieves current stock prices using Yahoo Finance when available
- Calculates total investment, current market value, profit or loss, and percentage return
- Saves portfolio results to `portfolio_summary.csv`

**Technologies:** Python 3, CSV module, file handling, and `yfinance`.

**Installation**

Install the required library:

```bash
python -m pip install yfinance
```

**How to run**

```bash
cd Task2_Stock_Portfolio
python portfolio.py
```

Follow the prompts to enter stock symbols, purchase prices, and share quantities. Type `DONE` when you have finished adding stocks.

**Dataset:** `constituents.csv` contains S&P 500 company information and ticker symbols. It is used to validate symbols and does not contain live stock prices.

**Disclaimer:** This project is for educational purposes only and does not provide financial advice. Stock price availability and accuracy depend on the external data provider.

## Purpose

This repository documents my practical Python programming work during the Datheon Python Programming Internship. It demonstrates programming fundamentals, data handling, input validation, and CSV file operations.
