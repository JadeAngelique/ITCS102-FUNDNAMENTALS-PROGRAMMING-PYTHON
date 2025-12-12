
import os

def print_statements():
        os.system('cls')
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        print("\t\t\t\t\t\t\tPRINT")
        print("The print () function prints the specified message to the screen, or other standard output device.")
        print("The message can be a string, or any other object.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        def printing():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tPRINTING")
                print("Printing in Python refers to the process of displaying text, numbers, or other data on the screen using the built-in print() function.")
                print("It sends information to the program’s standard output, allowing the user to see results, messages, or debugging information.")
                print("Example:")
                print('print("Hello World")')
                print("Output:Hello World")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def concatenation():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tCONCATENATION")
                print("Concatenation is the process of joining two or more strings together to form one continuous string")
                print("Example:")
                print("first = Hello")
                print("second = World")
                print("result = first + second")
                print("print(result)")
                print("Output: HelloWorld")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def string_formatting():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tSTRING FORMATTING")
                print("String formatting in Python is the process of creating strings.")
                print("that include variable values or expressions inside them in a clean, readable, and structured way.")
                print("It allows you to insert data into a string without manually concatenating pieces together.")
                print("Example:")
                print("name = Jade")
                print("age = 18")
                print('print(f"Hello, my name is {name} and Im {age} years old")')
                print("Output: Hello, my name is Jade and Im 18 years old")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
                print("MENU")
                print("1. Printing")
                print("2. Concatenation")
                print("3. String Formatting")
                print("4. Exit")

                choice1 = int(input("Enter a number you want to open: "))

                if choice1 == 1:
                        printing()
                        input("press any key to go back")
                
                elif choice1 == 2:
                        concatenation()
                        input("press any key to go back")

                elif choice1 == 3:
                        string_formatting()
                        input("press any key to go back")

                elif choice1 == 4:
                        print("EXITING")
                        break
                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue

                
def operators():
        os.system('cls')
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        print("\t\t\t\t\t\t\tOPERATORS")
        print("Operators are special symbols that perform operations on variables and values.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        def arithmetic():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tARITHMETIC OPERATORS")
                print("Arithmetic operators are symbols used to perform basic mathematical operations on numbers.")
                print("Examples: +, -, *, /, //, **, %")
                print("a = 3")
                print("b = 10")
                print('print(a + b)')
                print("Output: 13")
                print('print(a - b)')
                print("Output: 7")
                print('print(a * b)')
                print("Output: 30")
                print('print(a / b)')
                print("Output: 3.33")
                print('print(a // b)')
                print("Output: 3")
                print('print(a ** b)')
                print("Output: 1000")
                print('print(a % b)')
                print("Output: 1")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def comparison():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tCOMPARISON OPERATORS")
                print("Comparison operators are used to compare two values.")
                print("They return either True or False, depending on whether the comparison is correct.")
                print("Examples: ==,!=, >, <, >=, <= ")
                print("a = 10")
                print("b = 20")
                print("a == b")
                print("Output: False")
                print("a != b")
                print("Output: True")
                print("a < b")
                print("Output: True")
                print("a >= 5")
                print("Output: True")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        def logical():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tLOGICAL OPERATORS")
                print("Logical operators are used to combine or evaluate multiple conditions.")
                print("They return True or False, depending on the logic of the expressions.")
                print("Examples: and, or , not ")
                print('age = 18')
                print("has_id = True")
                print('print(age >= 18 and has_id)')
                print("Output: True")
                print('print(age < 18 or has_id)')
                print("Output: True")
                print('print(not has_id)')
                print("Output: True")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def assignment():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tASSIGNTMENT OPERATORS")
                print("Assignment operators in Python are used to assign values to variables.")
                print("They can also be used to update a variable’s value using arithmetic or bitwise operations.")
                print("Examples: =, +=, -=, *=, /=, //=, **=, %= ")
                print("a = 10")
                print("a += 5")
                print("print(a)")
                print("Output: 15")
                print("a *= 2")
                print("print(a)")
                print("Output: 30")
                print("a //= 3")
                print("print(a)")
                print("Output: 10")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
                print("MENU")
                print("1. Arithmetic Operators")
                print("2. Comparison Operators")
                print("3. Logical Operators")
                print("4. Assignment Operators")
                print("5. Exit")

                choice2 = int(input("Enter a number you want to open: "))

                if choice2 == 1:
                        arithmetic()
                        input("press any key to go back")

                elif choice2 == 2:
                        comparison()
                        input("press any key to go back")

                elif choice2 == 3:
                        logical()
                        input("press any key to go back")

                elif choice2 == 4:
                        assignment()
                        input("press any key to go back")
                
                elif choice2 == 5:
                        print("EXITING")
                        break

                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue

def variables():
        os.system('cls')  
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")              
        print("\t\t\t\t\t\t\tVARIABLES")
        print("A variable is a name that stores a value in memory so it can be used and changed later in a program.")
        print("It acts as a label that allows you to reference data without needing to know exactly where it is stored.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def string():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tSTRING")
                print("A string is a sequence of characters enclosed in quotes. It can contain letters, numbers, symbols, spaces—basically any text.")
                print("Strings are used for storing names, labels, descriptions, sentences, and anything that is not meant to be calculated numerically.")
                print("Examples:")
                print("name = Jade")
                print("greetings = Helloworld")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def integer():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tINTEGER")
                print("An integer is a whole number that does not contain any decimal or fractional part. It can be positive, negative, or zero.")
                print("Integers are commonly used for counting, indexing, loops, and any situation that requires exact whole-number values.")
                print("Examples: ")
                print("age = 20")
                print("debt = -2000")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def Float():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tFLOAT")
                print("A float is a number that contains a decimal point.")
                print("Floats are used when you need precision, such as measurements, scientific calculations, percentages, or divisions that produce decimal values.")
                print("Examples: ")
                print("price = 17.38")
                print("height = 6.7")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                
        def Boolean():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tBOOLEAN")
                print("A boolean stores only two possible values, True or False.")
                print("This type is especially useful for conditions, logic, comparisons, and decision-making in programs.")
                print("Examples: ")
                print("is_logged_in = True")
                print("comparison = 10 > 3")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def List():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tLISTS")
                print("A list is an ordered and changeable collection.")
                print("This means the items inside it keep their order, and you can update, remove, or add elements anytime.")
                print("Lists can store different types at the same time: numbers, strings, booleans, even other lists.")
                print("Examples:")
                print('fruits = ["apple", "banana", "mango"]')
                print('mixed_data = [25, "hello", 3.14, True]')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def dictionary():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tDICTIONARY")
                print("A dictionary stores information in key–value pairs.")
                print("Keys act like labels that allow you to find specific data quickly.")
                print("This structure is perfect for representing objects in the real world, like student profiles, product details, or structured data.")
                print("Example: ")
                print('student = {"name": "Jade", "grade": 90}')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
                os.system('cls')
                print("1. String")
                print("2. Integer")
                print("3. Float")
                print("4. Boolean")
                print("5. List")
                print("6. Dictionary")
                print("7. Exit")

                choice3 = int(input("Enter a number you want to open: "))

                if choice3 == 1:
                        string()
                        input("press any key to go back")

                elif choice3 == 2:
                        integer()
                        input("press any key to go back")

                elif choice3 == 3:
                        Float()
                        input("press any key to go back")

                elif choice3 == 4:
                        Boolean()
                        input("press any key to go back")

                elif choice3 == 5:
                        List()
                        input("press any key to go back")

                elif choice3 == 6:
                        dictionary()
                        input("press any key to go back")

                elif choice3 == 7:
                        print("EXITING")
                        break

                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue


def conditional():
        os.system('cls')
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        print("\t\t\t\t\t\t\tCONDITIONAL STATEMENT")
        print("A conditional statement is a feature in programming that checks a condition and then executes a specific block of code only if that condition is met.")
        print("If the condition is not met, the program can either skip the code or run a different block.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def ifstatement():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tIF STATEMENT")
                print("An if statement is a programming construct that allows you to make decisions based on certain conditions.")
                print("Example:")
                print("grade = 90")
                print("if grade >= 90:")
                print('   print("Excellent)')
                print("Output: Excellent")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def elifstatement():
                os.system('cls') 
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")       
                print("\t\t\t\t\t\t\tELIF STATEMENT")
                print("It can be used in conditional statements to check for multiple conditions.")
                print("Example:")
                print("grade = 85")
                print("if grade >= 90:")
                print('   print("Excellent)')
                print("elif grade >= 80:")
                print('   print("Good)')
                print("Output: Good")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def elsestatement():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tELSE STATEMENT")
                print("Else is a conditional statement used in programming to specify what should happen if a certain condition is not met. ")
                print("Example:")
                print("grade = 85")
                print("if grade >= 90:")
                print('   print("Excellent)')
                print("elif grade >= 80:")
                print('   print("Good)')
                print("else:")
                print('   print("Bad")')
                print("Output: Bad")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
                print("MENU")
                print("1. If Statement")
                print("2. Elif Statement")
                print("3. Else Statement")
                print("4. Exit")

                choice3 = int(input("Enter a number you want to open: "))

                if choice3 == 1:
                        ifstatement()
                        input("press any key to go back")

                elif choice3 == 2:
                        elifstatement()
                        input("press any key to go back")

                elif choice3 == 3:
                        elsestatement()
                        input("press any key to go back")

                elif choice3 == 4:
                        print("EXITING")
                        break

                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue

def loops():
        os.system('cls')
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        print("\t\t\t\t\t\t\tLOOPS")
        print("A loop is a programming structure that allows your code to repeat a block of instructions multiple times.")
        print("Instead of writing the same code over and over, a loop automatically cycles through the instructions until a certain condition is met.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def forloop():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tFOR LOOP")
                print("A for loop is used when you want to repeat something a specific number of times")
                print("or when you want to go through each item in a list, string, dictionary, or any sequence.")
                print("Example:")
                print('fruits = ["apple", "banana", "mango"]')
                print("for fruit in fruits:")
                print("print(fruit)")
                print("Output:")
                print("apple")
                print("banana")
                print("mango")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def whileloop():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tWHILE LOOP")
                print("A while loop keeps running as long as its condition stays true.")
                print("Example:")
                print("count = 1")
                print("while count <= 5:")
                print('    print("Number:", count)')
                print("    count += 1")
                print("Output:")
                print("Number: 1")
                print("Number: 2")
                print("Number: 3")
                print("Number: 4")
                print("Number: 5")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
                os.system('cls')
                print("MENU")
                print("1. For Loop")
                print("2. While Loop")
                print("3. Exit")

                choice4 = int(input("Enter a number you want to open: "))

                if choice4 == 1:
                        forloop()
                        input("press any key to go back")

                elif choice4 == 2:
                        whileloop()
                        input("press any key to go back")

                elif choice4 == 3:
                        print("EXITING")
                        break
                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue


def functions():
        os.system('cls')
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
        print("\t\t\t\t\t\t\tFUNCTIONS")
        print("A function is a reusable block of code that performs a specific task.")
        print("Functions help make your programs cleaner, shorter, more organized, and easier to understand.")
        print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def createfunction():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tCREATING A FUNCTION")
                print("You define a function using the def keyword.")
                print("Example:")
                print("def say_hello():")
                print('   print("Hello")')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def parameters():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tFUNCTIONS WITH PARAMETERS")
                print("Functions can accept information so they can work with different data.")
                print("Example:")
                print("def say_hello(name): ")
                print('   print("Hello, name)')
                print("say_hello(Jade)")
                print("Output: Hello, Jade")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        def returnvalues():
                os.system('cls')
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")
                print("\t\t\t\t\t\t\tFUNCTIONS WITH RETURN VALUES")
                print("A function can also return something back to you.")
                print("Example:")
                print("def add(a,b):")
                print("    return a + b")
                print("result = add(6,7)")
                print("print(result)")
                print("Output: 13")
                print("♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡﹏♡")

        while True:
     
                print("1. Create a Function")
                print("2. Function with Parameters")
                print("3. Function with Return Values")
                print("4. Exit")

                choice6 = int(input("Enter a number you want to open: "))

                if choice6 == 1:
                        createfunction()
                        input("press any key to go back")

                elif choice6 == 2:
                        parameters()
                        input("press any key to go back")

                elif choice6 == 3:
                        returnvalues()
                        input("press any key to go back")

                elif choice6 == 4:
                        print("EXITING")
                        break

                else:
                        print("Invalid")
                        input("press any key to go back")
                        continue
os.system('cls')
name = input("What is your name? ").upper()
course = input("What is your course? ").upper()

while True:
        os.system('cls')
        print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
        print("        \tWELCOME TO MY PROGRAM        ")
        print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
        print(f"Hello! {name} from {course}.")
        print("Thank you for using my final project!")
        print("I hope you enjoy exploring this program.")
        print("❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
        print("\tMENU")      
        print('1. Print')
        print("2. Operators")
        print("3. Variables")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Function")
        print("7. Exit")


        choice = int(input("Enter a number you want to open: "))

        if choice == 1:
                print_statements()
                input("press any key to go back")

        elif choice == 2:
                operators()
                input("press any key to go back")

        elif choice == 3:
                variables()
                input("press any key to go back")

        elif choice == 4:
                conditional()
                input("press any key to go back")

        elif choice == 5:
                loops()
                input("press any key to go back")

        elif choice == 6:
                functions()
                input("press any key to go back")
        
        elif choice == 7:
                print("EXITING")
                break

        else:
                print("invalid")
                input("press any key to go back")
                continue