#Code by Kyle Mann kyle.mann1@snhu.edu
# Here you can practice and get help on the exercise to find the smallest of 3 integers. Add code to do what the comments describe.
# For each of three numbers, prompt for it to be input and assign a variable to the integer value of what was input.
num_1 = int(input("Enter the first number."))
num_2 = int(input("Enter the second number."))
num_3 = int(input("Enter the third number."))
# Add conditional logic to calculate the smallest number. Your code should work even if two or all three of the numbers are equal.
if num_1 <= num_2 and num_1 <= num_3:
    smallest_num = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    smallest_num = num_2
else:
    smallest_num = num_3
# Print the smallest number.
print ("The smallest number is ",smallest_num)