import random

## Defining the bet and how many lines we want to bet on
MAX_LINES = 3
MAX_BET= 100
MIN_BET = 1

## Defining the reels of the slot machine
ROWS = 3
COLS = 3
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


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    ## start the betting on line 1
    for line in range(lines):
        ## checking the symbol that is on the first column of the current row
        symbol = columns[0][line]
        ## checking if the first symbol is the same as the symbols in all the other columns in the current row
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            ## the line the user won
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    ## Adding all the symbols to the all_symbol list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    ## Selecting the values that is going to every single column
    columns = []
    ## generating a column for every column that we have
    for _ in range(cols):
        ## making a copy of the all_symbols list so when we use a symbol, then we remove it from the list 
        current_symbol = all_symbols[:]
        ## pick random values for each row
        column = []
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns

## transposing
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end= " | ")
            else:
                print(column[row], end="")
        ## goes to the next line
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the numbers you want to bet on eahc line (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("How much do you want to bet (" + str(MIN_BET) + "-" + str(MAX_BET) + ")? ")
        if bet.isdigit:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a number between ${MIN_BET} - ${MAX_BET}.")
    return bet
    
## each game
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not enough to be that amount. Your current balance is ${balance}")
        else:
            break
    print(f"You're betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on line", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin or q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
