
import random

#global constant values
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

#dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# [A] [A] [A]
# [A] [A] [A]
# [B] [B] [B]
# [B] [B] [B]
# [B] [B] [B]
# [B] [B] [B]
# [C] [] [A]
# [A] [A] [A]
# [A] [A] [A]
# [A] [A] [A]
# [A] [A] [A]
# [A] [A] [A]
# [A] [A] [A]
# [A] [A] [A]

def get_slot_machine_spin(rows, cols, symbols):
    
    #list
    all_symbols = []
    
    #symbol = A, symbol_count = 2
    # items() give you both key and value associated with a dictionary.
    for symbol, symbol_count in symbols.items():
        
        # underscore is used since we don't care about the count
        for _ in range(symbol_count):
            
            #add symbol based on what value it's been assigned in the dictionary.
            all_symbols.append(symbol)
            
    #columns = [[], [], []]
    
    columns = []
    
    #for each col, we want to add a row. for each row we want to choose a random symbol.
    for col in range(cols):
        
        col = []
        # ":" copies list since we want to remove values and not re-use the same list.
        current_symbol = all_symbols[:]
        
        for _ in range(rows):
            
            #choose random symbol
            value = random.choice(current_symbol)
            #remove the chosen symbol from the list
            current_symbol.remove(value)
            col.append(value)
            
        columns.append(col)    
        
    return columns

def print_slot_machine(columns):
    
    #transposing
    for row in range(len(columns[0])):
        #enumerate gives you both the index and item
        for i, col in enumerate(columns):
            print(col[row],)  

#grab how much user would like to deposit
def get_deposit():
    while True:
        amount = input("How much $ would you like to deposit? ")
        
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:       
                break
            else:
                print("Amount must be greater than zero.")
            
        else:
            print("Please enter a number")   
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter a number of lines (1-" + str(MAX_LINES) + "): ")
        
        if lines.isdigit():
            lines = int(lines)
            
            if 1 <= lines <= MAX_LINES:       
                break
            else:
                print("Number must be greater than zero.")
            
        else:
            print("Please enter a number")   
    return lines


def get_bet():
    while True:
        bet = input("What would you like to bet on each line? ")
        
        if bet.isdigit():
            bet = int(bet)
            
            if MIN_BET <= bet <= MAX_BET:       
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET})")
            
        else:
            print("Please enter a number")   
    return bet




#main function
def main():
    user_balance = get_deposit()
    number_of_lines = get_number_of_lines()

    
    while True:
        user_bet = get_bet()
        total_bet = user_bet * number_of_lines
        
        if user_balance > total_bet:
            print(f"You are betting ${user_bet} on {number_of_lines}.")
            print(f"Total lines is equal to ${total_bet}.")
            break
        else:
            print("You don't have enough money to bet!")
            exit()

            



main()