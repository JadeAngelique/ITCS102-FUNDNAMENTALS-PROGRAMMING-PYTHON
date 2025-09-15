num =eval(input("Enter any number:"))
result = 1
for i in range(num, 0, -1):
    result *= i

print("The factorial of the number is", result)
