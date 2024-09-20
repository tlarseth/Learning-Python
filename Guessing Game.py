import random

#seedVal = int(input("What seed should be used? "))
#random.seed(seedVal)

lower = int(input("What is the lower bound?"))
upper = int(input("What is the upper bound?"))

while upper <= lower:
    print("Lower bound must be less than upper bound.")
    lower = int(input("What is the lower bound?"))
    upper = int(input("What is the upper bound?"))

rand_num = random.randint(lower, upper)

while True:

    guess = int(input("What is your guess?"))

    while guess < lower or guess > upper:
        print("What is your guess?")
        guess = int(input("What is your guess?"))

    if guess == rand_num:
        print("You got it!")
        break

    if guess < rand_num:
        print("Nope, too low.")
    else:
        print("Nope, too high.")