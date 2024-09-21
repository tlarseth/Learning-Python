# Created by T-Lar Seth of the Gamer's Guild©
# Ask user for their name
name = input("What's your name? ").strip().title()

#split user name into first and last names
first,last = name.split(" ")

# Say hello to user
print (f"Hello, {first}")