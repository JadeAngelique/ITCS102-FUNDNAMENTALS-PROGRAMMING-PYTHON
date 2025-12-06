from activity25_1 import *
from activity21.2 import *
greet_user = input("Enter your name:")

print(f"Hello, {greet_user}! Welcome to File Compiler")

Rainer = True

while Rainer == True:
   print("Select the activity you want to access:"
   print("A-Activity1\nB-Activity2\nC-Activity3\nD-Activity4\nE-Exit")

   choice = input("What acctivity do you want to access?").lower()

   if  choice == 'a':
       activity1()
       continue
   elif choice == 'b':
       activity2()
       continue
    elif choice == 'c': 
        activity3()
        continue
        elif choice == 'd':
            activity4()
            continue
        elif choice == 'e':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
