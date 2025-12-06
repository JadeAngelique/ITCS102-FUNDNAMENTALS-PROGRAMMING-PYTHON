print("Adding Data to Dictionary")
print("----------------------------")
cont = True

empty_dictionary = {}

def print_color():
    for j, a in empty_dictionary.items():
        print(f"{j} : {a}")

while cont == True:
    color = input("Enter Color: ")
    code = input("Enter Code: ")
    empty_dictionary[color] = code
    print_color()
    choice = input("Do you want to add more data? (yes/no/show): ")
    if choice == 'yes':
        print("Continuing to add data...")
        continue
    elif choice == 'no':
        print("Exiting the program...")
    elif choice == 'show':
        print_color()
        continue
    else:
        print("Invalid choice. Exiting the program...")
        break
