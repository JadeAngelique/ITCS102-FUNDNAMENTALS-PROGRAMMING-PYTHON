add_to_cart = []
ask = input("Do you want to add an item to your cart? (yes/no): ").lower()

if ask == "yes":
    print("Item added to cart.")
    print("Current items in cart:", add_to_cart)
    print("More - to add more items\nView - to view cart\nCheckout - to proceed to checkout")
    type = input("What do you want to do? ").lower()
    while type != "checkout":
        if type == "more":
            item = input("Enter item to add: ")
            add_to_cart.append(item)
            print("Item added to cart.")
            print("Current items in cart:", add_to_cart)
        elif type == "view":
            print("Current items in cart:", add_to_cart)
        else:
            print("Invalid option. Please choose More, View, or Checkout.")
        type = input("What do you want to do? ").lower()
