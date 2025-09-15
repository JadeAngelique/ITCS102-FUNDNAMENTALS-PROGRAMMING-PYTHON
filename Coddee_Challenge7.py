total = 0

for x in range(10):
    num = eval(input(f"Enter number {x+1}: "))
    if num % 2 != 0:  
        total += num

print("The sum of odd numbers is:", total)