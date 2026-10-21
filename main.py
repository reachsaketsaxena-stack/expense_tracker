expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def show_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    for number, item in enumerate(expenses, start=1):
        print(f"{number}. {item['category']}: {item['amount']}")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print("Total spent:", total)

while True:
    print("\n1. Add expense")
    print("2. Show all expenses")
    print("3. Show total")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Please enter a number.")
            continue
        category = input("Category: ")
        add_expense(amount, category)
        print("Added.")
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")