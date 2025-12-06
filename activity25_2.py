def activity4():
    num = eval(input("Enter a number: "))
    factorial_value = 1
    for rainer in range (num,0,-1):
        factorial_value *= rainer
    print(f"The Factorial of{num} is {factorial_value}")