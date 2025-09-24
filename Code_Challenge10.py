print("\t\t", end=" *")
for j in range(1, 11):
    for k in range(10, j, -1):
        print(" ", end=" ")
    for l in range(1, j):
        print("*", end=" ")
    for m in range(1, j):
        print("*", end=" ")
    print()