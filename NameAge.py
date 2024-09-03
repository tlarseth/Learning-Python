# Asks user for their name and age
user_name = input('What is your name?')
user_age = int(input('How old are you?'))

# Pull birth year from age variable
user_year = (2024-user_age)

# Outputs the user's name and year of birth with a greeting
print ('Hello {}!  You were born in {}.'.format(user_name, user_year))