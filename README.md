# Hangman Game (Pendu) - An Old Python Project

## Overview
This is a **Hangman Game (Pendu)** created using **Python** and **Tkinter**. It is one of my older projects from five years ago and serves as a great way to practice GUI programming, logic handling, and game development in Python. The game selects a random word from a file and challenges the player to guess it before they run out of attempts.

## Features
- **Graphical User Interface (GUI)** built with Tkinter
- **Random word selection** from a text file
- **Keyboard input simulation** using buttons
- **Win/Loss detection** with different screens for success and failure
- **Basic animations** with images

## Technologies Used
- **Python**
- **Tkinter (for GUI)**
- **Random module** (to select words)

## How It Works
1. The player enters their name.
2. A random word is chosen from `list.txt`.
3. The player guesses letters by clicking buttons.
4. Incorrect guesses add to a failure count (max 5 mistakes allowed).
5. If the player guesses the full word, they win.
6. If they make too many mistakes, they lose.

## Installation & Running the Game
1. **Install Python** (if not already installed).
2. Download the project files and make sure `list.txt` is present.
3. Run the script:
   ```sh
   python hangman.py
   ```
