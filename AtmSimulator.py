balance = 20000
pin = 2323
while True:
    print("1. Deposit Amount")
    print("2. Check Balance")
    print("3. Withdraw money")
    print("4. Exit")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        amount = int(input("Enter the amount:"))
        balance += amount
        print(f"Total Balance:{balance}")
    elif choice == 2:
        upin = int(input("Enter the Pin"))
        if upin == pin:
            print(f"Balance:{balance}")
        else:
            print("Pin Incorrect")
    elif choice == 3:
        upin = int(input("Enter the Pin"))
        if upin == pin:
           amount = int(input("Enter the Amount to Withdraw:"))
           if(amount > balance):
               print("No sufficient balance")
           else :
               balance -= amount
               print(f"Available Balance:{balance}")
    else:
        print("Thankyou for visiting")

else:
    print("Invalid choice")