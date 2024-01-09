import random

# Constants
MAX = 3
MAXBET = 100
MINBET = 10

ROW = 3
COL = 3

# Symbol count and value dictionaries
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

name = input("Please tell us your name here:")


# Function to check for winning combinations
def checkwin(columns, lines, bet, values):
    win = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        # Checking if all symbols in a line are the same
        for column in columns:
            symbol_check = column
            if symbol != symbol_check:
                break
        else:
            win += values[symbol] * bet  # Calculating win amount
            win_line.append(line + 1)  # Adding winning line

    return win, win_line


# Function to simulate spinning the slot machine
def spinmac(rows, cols, symbols):
    allsymbol = []
    # Creating a list of symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            allsymbol.append(symbol)

    columns = []
    # Creating columns with randomized symbols
    for _ in range(cols):
        column = []
        currentsy = allsymbol[:]
        for _ in range(rows):
            vale = random.choice(currentsy)
            currentsy.remove(vale)
            column.append(vale)

        columns.append(column)

    return columns


# Function to display the slot machine grid
def displayslot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# Function for user deposit
def deposite():
    while True:
        try:
            amt = int(input("What is the amount you are ready to deposit? : $"))
            if amt > 0:
                break
            else:
                print("The amount must be significant.")
        except ValueError:
            print("Please enter a valid amount.")

    return amt


# Function to get the number of lines to bet on
def getlines():
    while True:
        try:
            lines = int(input(f"What is the number of lines you are ready to bet on (1-{MAX})? : "))
            if 1 <= lines <= MAX:
                break
            else:
                print("Enter a valid number of lines.")
        except ValueError:
            print("Please enter a valid number.")

    return lines


# Function to get the betting amount
def getbet():
    while True:
        try:
            amt = int(input(f"What is the amount you are ready to bet? (${MINBET} - ${MAXBET}): $"))
            if MINBET <= amt <= MAXBET:
                break
            else:
                print(f"The bet must be between ${MINBET} - ${MAXBET}.")
        except ValueError:
            print("Please enter a valid amount.")

    return amt


# Function to play the game for one round
def spin_game(balance):
    lines = getlines()

    while True:
        bet = getbet()
        total = bet * lines
        if total > balance:
            print("You do not have enough balance to bet.")
        else:
            break

    print(f"You have bet ${bet} on {lines} lines. The total amount in the pot is ${total}")

    slots = spinmac(ROW, COL, symbol_count)
    displayslot(slots)
    winnings, winnings_lines = checkwin(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings} on lines", *winnings_lines)

    return winnings - total


# Main function to start the game
def main():

    balance = deposite()
    while True:
        print(f"Your current balance is ${balance}.")
        spin = input("To begin the game press enter and to quit the game press Q: ")

        if spin == "Q":
            break

        balance += spin_game(balance)

    print(f"You are leaving with ${balance}.")
    print(f"Have a good day, {name}!")

# Start the game
main()
