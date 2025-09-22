# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Implement a text-based Hangman game where the program randomly selects a word and the player guesses letters until they reveal the word or run out of attempts. Practice string manipulation, loops, conditionals, and handling user input in a clear, user-friendly loop.

## 📝 Tasks

### 🛠️	Implement core Hangman gameplay

#### Description
Build the main Hangman game loop: randomly choose a secret word, accept single-letter guesses from the player, reveal correctly guessed letters in the masked word display, and track remaining incorrect attempts. The game should end with a clear win or lose message.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list containing at least 10 words.
- Display the player's current progress using underscores and spaces for unrevealed letters (e.g., `_ a _ _ e`).
- Accept single-letter guesses (case-insensitive). If a letter has already been guessed, inform the player and do not consume an attempt.
- Decrement the remaining attempts only for incorrect and previously unguessed letters. Start with a reasonable default (suggested: 6 attempts).
- Display the list of incorrect guesses and the number of attempts remaining after each turn.
- End the game when the player correctly reveals all letters (win) or when attempts reach zero (lose). On game end, display an appropriate win/lose message and reveal the secret word.

Example gameplay (user input lines prefixed with >):

```
Secret word: _ _ _ _ _
Incorrect guesses: 
Attempts remaining: 6
Enter a letter: > a
Correct! Progress: _ a _ _ _
Incorrect guesses: 
Attempts remaining: 6
Enter a letter: > z
Incorrect. Progress: _ a _ _ _
Incorrect guesses: z
Attempts remaining: 5
```

### 🛠️	Add polish and optional enhancements

#### Description
Extend and polish your core implementation by adding useful features for a better player experience: validate inputs, support guessing the full word, provide difficulty options, and make the code modular with functions.

#### Requirements
Completed program should (pick at least two enhancements):

- Provide a difficulty selection that adjusts starting attempts (e.g., Easy=10, Medium=6, Hard=4).
- Allow the player to guess the full word at any time; a correct full-word guess wins immediately, an incorrect full-word guess may cost 1 or more attempts (document your choice).
- Show simple ASCII-art hangman or progressive visual feedback corresponding to remaining attempts.
- Validate input so only alphabetic single-character guesses are accepted; prompt again on invalid input without consuming attempts.
- Offer a replay option at the end of a round to play again without restarting the program.
- Structure the program into functions (e.g., select_word, display_progress, process_guess, main) and include brief comments/docstrings explaining the main functions.

Example enhancement interaction:

```
Choose difficulty (Easy/Medium/Hard): > Medium
Attempts set to 6.
Enter a letter or guess the full word: > python
Incorrect full-word guess. Attempts remaining: 5
```
