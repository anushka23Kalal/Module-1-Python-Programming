print("------Expense Tracker-------")
budget=float(input("Enter Budget: "))
expenses=[]

def addexpense():
    name=input("Enter expense name: ")
    amount=float(input("Enter amount: "))
    category=input("Enter Category: ")

    expense={
        "name":name,
        "amount":amount,
        "category":category
    }
    expenses.append(expense)
    print("Expense Added Successfully")

def checkBalanceBudget():
    spent=0
    for ex in expenses:
        spent+=ex["amount"]
    balance=budget-spent
    return balance

def viewExpenses():
    total_exp=0
    i=1
    for exp in expenses:
        total_exp+=exp["amount"]
        print(i,". ",exp["name"]," ",exp["amount"]," ",exp["category"])
        i=i+1
    print("Total expense: ", total_exp)


while True:
    print("1. Add Expense")
    print("2. Check Budget")
    print("3. View Expenses ")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        addexpense()
    elif choice==2:
        print(checkBalanceBudget())
    elif choice==3:
        print(viewExpenses())
    elif choice==4:
        print("Thank you..!")
        break
    else:
        print("Invalid Input")