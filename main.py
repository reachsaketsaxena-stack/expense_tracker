expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

add_expense(250, "food")
add_expense(1200, "books")

total = sum(item["amount"] for item in expenses)
print("Total spent:", total)