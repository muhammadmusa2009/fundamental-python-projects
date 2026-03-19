print("Hello User! Welcome to the Trip Expense Calculator.\n")

# Ask for total budget
budget = int(input("Enter your total budget for the trip (numbers only): $"))
print(f"Your total budget is: ${budget}\n")

# Initialize remaining budget
remaining = budget

# Define categories
categories = ["Travelling", "Hotels", "Meals", "Shopping", "Other Miscellaneous Expenses"]

for category in categories:
    expense = int(input(f"Enter your {category} expense: $"))
    
    if expense > remaining:
        print(f"You have exceeded your budget! Remaining: ${remaining}\n")
        break
    elif expense == remaining:
        print(f"You have used all your funds on {category}.")
        remaining = 0
        break
    else:
        remaining -= expense
        print(f"Remaining budget after {category}: ${remaining}\n")

if remaining > 0:
    print(f"Trip completed! You have ${remaining} left.")