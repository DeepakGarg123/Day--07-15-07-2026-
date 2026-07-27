secret_number = 53
chances = 3
guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("  You guessed the correct number.")
else:
    chances -= 1

    if guess < secret_number:
        print("  Low")
    else:
        print("  High")

    print("Remaining Chances:", chances)

    guess = int(input("\nEnter your guess: "))

    if guess == secret_number:
        print("  You guessed the correct number.")
    else:
        chances -= 1

        if guess < secret_number:
            print("  Low!")
        else:
            print("  High!")

        print("Remaining Chances:", chances)   
        

        guess = int(input("\nEnter your guess: "))

        if guess == secret_number:
            print("  You guessed the correct number.")
        else:
            if guess < secret_number:
                print("  Low Number")
            else:
                print("  High Number")

            print("\n Game Over!")
            print("The correct number :", secret_number)