import random

MAX_LINES =  3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for i in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for i in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("What would you like to deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amont must be greater than 0.")
        else:
            print("Please enter a whole number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter numer from 1-" + str(MAX_LINES) + ".")
        else:
            print("Please enter a whole number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between €{MIN_BET} and €{MAX_BET}.")
        else:
            print("Please enter a whole number")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Bet exceeds balance. Your balance is €{balance}.")
        else:
            break

    print(f"You are betting €{bet} on {lines} lines. Total amount to bet is €{total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)



main()