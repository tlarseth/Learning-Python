import random

lower = int(input("What is the lower bound?"))
upper = int(input("What is the upper bound?"))

while upper <= lower:
    print("Lower bound must be less than upper bound.")
    lower = int(input("What is the lower bound?"))
    upper = int(input("What is the upper bound?"))

rand_num = random.randint(lower, upper)
counter = 0
while True:

    guess = int(input("What is your guess?"))
    counter += 1
    while guess < lower or guess > upper:
        print("What is your guess?")
        guess = int(input("What is your guess?"))



    if guess == rand_num:
        print("You got it!")
        print ("It took you {} tries to get it".format(counter))
        break

    if guess < rand_num:
        print("Nope, too low.")
    else:
        print("Nope, too high.")