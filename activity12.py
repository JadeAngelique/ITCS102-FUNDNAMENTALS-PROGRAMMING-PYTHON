print("Hello!Jade Here")
for i in range(1,6,1):
    for x in range(5,i,-1):
        print(" ", end=" ")
    for y in range(1,i+1,1):
        print("*", end=" ")
    print()