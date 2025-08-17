def diposit():
    while True:
        amount = input("How much deposit do you want? ")
        if amount.isdigit():
            amount = int(amount)
            if amount >100000:
                print("Max diposit limit 100000")
            elif amount > 0:
                return amount
            
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a valid number.")

def place_bet(balance):
    while True:
        bet = input(f"You have ${balance}. How much do you want to bet? ")
        if bet.isdigit():
            bet = int(bet)
            print("Max bet limit 10000")
            if  bet >100000:
               print("Max bet limit 10000")
            elif 0 < bet <= balance:
                 return bet
            else:
                print("insufficient balance.")
        else:
            print("Please enter a valid number.")

# Step 1: Get deposited amount
deposited_amount = diposit()
bonus = deposited_amount * 0.10
balance = deposited_amount + bonus

print(f"You deposited: ${deposited_amount}")
print(f"You got a bonus of: ${bonus}")
print(f"Your total wallet balance is: ${balance}")

# Step 2: Place a bet
bet = place_bet(balance)
print(f"You placed a bet of: ${bet}")
