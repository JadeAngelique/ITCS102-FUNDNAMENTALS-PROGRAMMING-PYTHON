Fruits = ["Apple", "Banana", "Cherry", "Date", "strawberry"]
print(Fruits)
print(Fruits[2])
print(Fruits[-1])
print(Fruits[1:4])


Fruits.insert(3, "Mango")
print (Fruits)

Fruits.pop()
print(Fruits)

Fruits.remove("Banana")
print(Fruits)

Fruits.sort()
print(Fruits)

Fruits.reverse()
print(Fruits)

for fruit in Fruits:
    print(f"I want to make  a smoothie with {fruit}")

print(Fruits[-4:-1])