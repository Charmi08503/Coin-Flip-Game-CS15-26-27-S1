import random

incorrect_guesses = 0

while incorrect_guesses < 3:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Guess heads or tails: ")
        guess = guess.lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input. Please enter heads or tails.")

    print("The coin landed on", coin + ".")

    if guess == coin:
        print("Correct!")
        incorrect_guesses = 0
    else:
        incorrect_guesses += 1
        print("Incorrect!")
        print("Incorrect guesses in a row:", incorrect_guesses)

print("Game over! You made 3 incorrect guesses in a row.")