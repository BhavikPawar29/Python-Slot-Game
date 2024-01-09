# Slot Machine Game

Welcome to the Slot Machine Game! This Python-based game allows users to enjoy the thrill of a virtual slot machine, placing bets, and winning based on symbol combinations.

## Overview

This project implements a simple yet engaging slot machine game where players can bet on different lines and symbols to win virtual currency. The game utilizes Python's random module to simulate spinning reels and checks for winning combinations based on predefined symbol values.

## Features

- **Player Interaction**: Players can personalize their gaming experience by entering their name at the start of the game.
- **Deposit System**: Users can initiate the game by depositing an initial amount of virtual currency.
- **Betting Options**: Players can choose the number of lines to bet on and the betting amount, adhering to specified limits.
- **Slot Machine Simulation**: The game simulates spinning reels with randomized symbols for each play.
- **Win Calculation**: Based on the chosen lines and symbol combinations, the game calculates and displays the winnings.
- **Game Progression**: Allows continuous gameplay until the player decides to quit.
- **Balance Tracking**: Keeps track of the player's balance throughout the game.

## Getting Started

### Prerequisites

- Python 3.11

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/BhavikPawar29/Python-Slot-Game.git
    cd Unlocked_Challenge_4
    ```

2. Run the Python script `slot_machine.py`:

    ```bash
    python slot_machine.py
    ```

### Usage

1. **Initial Setup**:
    - Input your name to personalize the gaming experience.
    - Deposit an initial amount to start playing.

2. **Gameplay**:
    - Press Enter to start the game.
    - Choose the number of lines and bet amounts as per the specified limits.
    - Spin the slot machine and await the results.
    - Winnings will be displayed based on the symbol combinations.

3. **Quitting the Game**:
    - To exit the game, type 'Q' when prompted during your turn.

## Files

- `SlotGame.py`: Contains the Python code for the slot machine game.
- `README.md`: Provides information about the project.

## Structure

- `MAX`, `MAXBET`, `MINBET`: Constants defining the maximum lines and bet amounts.
- `ROW` and `COL`: Define the slot machine's grid structure.
- `symbol_count` and `symbol_value`: Dictionaries defining symbols, their counts, and values.
- Functions:
    - `checkwin`: Checks for winning combinations based on the grid.
    - `spinmac`: Simulates spinning the slot machine with randomized symbols.
    - `displayslot`: Displays the current state of the slot machine grid.
    - `deposite`, `getlines`, `getbet`: Functions to handle user inputs.
    - `spin_game`: Runs the game logic for a single round.
    - `main`: Acts as the main game loop.

## Contributors

- [Bhavik Pawar](https://github.com/BhavikPawar29)

## Acknowledgements

Special thanks to Tech With Tim for inspiration and guidance that contributed to the development of this project.

Here's the link:https://youtu.be/th4OBktqK1I?si=w5LYeJ-VGVHmgrwK
