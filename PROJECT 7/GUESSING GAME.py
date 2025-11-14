
secret_number = random.randint(0, 10)
guess = input("Guess a number between 0 and 10: ")
if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    else:
        print(f"Wrong guess. The correct number was {secret_number}.")
else:
    print("Please enter a valid number.")
