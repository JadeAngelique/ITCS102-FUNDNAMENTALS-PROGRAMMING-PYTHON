print("Welcome to makeup  store")
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the makeup store.")
bill = float(input("Enter your total bill amount: "))
member = input("Do you have a membership card? (yes/no): ")

if  member == "yes":
    discount = bill * 0.20
    final_bill = bill - discount
    print("You have a membership card. A 20% discount has been applied.")
else:
    final_bill = bill
    print("You do not have a membership card. No discount applied.")