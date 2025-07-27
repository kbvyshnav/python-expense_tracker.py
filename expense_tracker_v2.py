def show_menu():

    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Show Category Summary")
    print("5. Exit")


def menu():
    expenses=[]
    while True:
        show_menu()

        choice=int(input("Enter your choice:"))
        if choice==1:
            print("You chose Add Expense")

            amount=int(input("Enter your expense amount :"))
            category=input("Enter your expense category : ")
            expenses.append({"Amount":amount, "Category":category})
            print(expenses)


        elif choice==2:
             
             print("You chose show expenses :")

             for index,expense in enumerate(expenses,start=1):
                 print(f"{index}. Amount:{expense['Amount']}, Category:{expense['Category']}")
                       

        elif choice ==3:
             print("You chose Show Total")

             if not expenses:                
                print("No expenses to calculate, please add expenses first!")
             else:
                 amount=[expense['Amount'] for expense in expenses]
                 total=(sum(amount))
                 average=(total/len(amount))
                 highest=(max(amount))
             
                 print(f"Total Expense: {total}")
                 print(f"Average Expense: {average}")
                 print(f"Highest Expense: {highest}")
               
                
        elif choice == 4:
                print("You chose Show Category Summary")

                if not expenses:
                    print("No expenses to show. Please add some expenses first!")
                else:
                    category_summary = {}

                    for expense in expenses:
                        category = expense['Category']
                        amount = expense['Amount']

                        if category in category_summary:
                            category_summary[category] += amount
                        else:
                            category_summary[category] = amount

                    print("Category Summary:")
                    for cat, total in category_summary.items():
                        print(f"{cat}: ₹{total}")


        else:
            print("Exited !!")
            break
 
menu()
             

