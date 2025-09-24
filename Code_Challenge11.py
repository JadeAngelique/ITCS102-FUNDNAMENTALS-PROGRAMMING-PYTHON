print("\t\t", end=" *")
for j in range(1, 11,):
    for a in range(10,j, -1):
        print(" ", end=" ")
    for d in range(1, j,):
        print("*", end=" ")
    for e in range(1, j,):
        print("*", end=" ")
    print()


for h in range(9, 0, -1):
    for a in range(10, h, -1):
        print(" ", end=" ")
    for d in range(1, h):
        print("*", end=" ")
    for e in range(1, h):
        print("*", end=" ")
    print("*")