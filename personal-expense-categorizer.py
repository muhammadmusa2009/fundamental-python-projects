#Welcome the user
print("Hello User. Welcome to the expense calculator! ")
#Ask for the budget
budget = int(input("What is your total budget for the trip? (in number only please) "))
print("So your total budget is:", str(budget) + "$")
#Categories
#Ask for the travelling
travelling = int(input("What is your travelling expense? "))
if travelling < budget:
    print( str(budget - travelling) + "$" + "is the remaining budget. ")
#Hotels
    hotels = int(input("What is your cost of living for the entire trip? "))
    rest = budget - travelling
    if hotels < (rest):
        print( str(rest - hotels) + "$" "is the remaining amount. ")
        rest1 = rest - hotels
#Meals
        meals = int(input("What is your cost of all meals for the entire trip? "))
        if meals < rest1:
            print(str(rest1 - meals) + "$" + "is your remaining amount.")
            rest2 = rest1 - meals
#Shopping 
            shopping = int(input("What is your total cost of shopping for entire trip?"))
            if shopping < rest2:
                print(str(rest2 - shopping) + "$" + "is the remaining amount. ")
                rest3 = rest2 - shopping
#Other Miscelanious Expenses     
                others = int(input("What are your other miscelanious expense for the trip? "))
                if others < rest3:
                    print(str(rest3 - others) + "$" + "is your remaining amount. ")
                elif others == rest3:
                    print("You have used all your funds, now.")
                else:
                    print("You have exceeded the limit. ")
            elif shopping == rest2:
                print("You have used all your funds, now. ")
            else:
                print("You have exceeded the limit. ")
        elif meals == rest1:
            print("You have used all your funds, now. ")
        else:
            print("You have exceeded the limit.")              
    elif hotels == (rest):
        print("You have used all your funds, now. ")
    else:
        print("You have exceeded the limit. ")
elif travelling == budget:
    print("You have used all your funds, now. ")
else:
    print("You have exceeded the limit. ")