def greeter(name):
    print(f"Hello, {name}! Welcome to the makeup store.")   

def summation(j):
    sum = 0
    for a in range(j, 0, -1):
        sum += a
        print(f"Adding {a}, current sum: {sum}")

        greeter("Jade")
        greeter("Pilarca")
        summation(11)
        summation(12)
        summation(5)