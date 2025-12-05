import random



num = random.randint(1,10)


tries = 4

while tries != 0:
    guess_num = eval(input("Guess a number between 1 and 10: "))
    tries -= 1

    if guess_num != num:
        print("Wrong Guess! Try Again.")
        print("You have", tries, "tries left.")

    elif guess_num == num:
        print("Congratulations! You guessed the correct number.")
        break


if tries == 0:
    print("Sorry, you've used all your tries. The correct number was", num)
    