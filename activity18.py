num = 10
for outer in range(1,6,1):
    for inner in range(outer + 1, 6):
        print(num, end=" ")
        num -= 1
    print()

for outer in range(1,11,1):
    for inner in range(1,outer):
        print(inner, end=" ")
    print()

for outer in range(1,11,1):
    for inner in range(1,outer):
        print(inner, end=" ")
    print()

num = 1
for outer in range(1,5,1):
    for inner in range(1,outer + 1):
        print(num, end=" ")
        num += 1
    print()

