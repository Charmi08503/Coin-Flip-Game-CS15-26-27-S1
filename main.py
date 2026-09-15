import random

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("What is your guess? ")
        guess = guess.lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input.")

    if guess == coin:
        print("Correct!")
    else:
        print("Incorrect!")

    print("The coin landed on", coin + ".")