MAX_LINES =  3


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
            if 1 <= lines <= 3:
                break
            else:
                print("Please enter numer from 1-" + str(MAX_LINES) + ".")
        else:
            print("Please enter a whole number")
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()

main()