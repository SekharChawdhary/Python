def diposit():
    while True:
        amount = input("How much diposit do you want?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("Enter a number")
    return amount
diposited_amount=  diposit()
print(f"you diposited amount: {diposited_amount}")
bonus= diposited_amount *0.10
print(f"you Got bonus: {bonus}")
print(f"{diposited_amount + bonus} Total Wallet Balance")


    