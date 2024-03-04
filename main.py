
#global constant values
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

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
        bet = input(f"Enter a bet (Must be between ${MIN_BET} - ${MAX_BET}) ")
        
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
    user_bet = get_bet()
    
    print("amount is: $" + str(user_balance) + "\n")
    print("number of lines is: " + str(number_of_lines) + "\n")
    print(f"number of lines is: ${user_bet}" + "\n")


main()