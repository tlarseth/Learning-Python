# Coded by Kyle Mann kyle.mann1@snhu.edu
# get name as a string
user_name = str(input("What is your name?"))
# get age as an int
user_age = int(input("What is your age?"))
# calculate birth year
from datetime import date
current_year = date.today().year
user_year = (current_year - user_age)
# print greeting
print ("Hello {}!  You were born in {}.".format(user_name, user_year))