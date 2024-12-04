#Created by Dae'Loki
#Gamer's Guild©



# ask for input for employee payrate and total hours worked
emp_payrate = float(input("What is the employee's payrate?"))
emp_total_hours = float(input("What is the employee's total hours for the week?"))

# check if total hours are over 40 hours
# If they are create new variable for OT hours and reg hours

if emp_total_hours > 40:
    reg_hours = 40
    ot_hours = emp_total_hours - 40
else:
    reg_hours = emp_total_hours
    ot_hours = 0

# calculate pay for each variable

reg_paycheck = float(reg_hours * emp_payrate)
ot_payrate = emp_payrate * 1.5
ot_paycheck = ot_hours * ot_payrate
total_paycheck = (reg_paycheck + ot_paycheck)
# Output total paycheck

print ("Your gross pay will be ${} based on {} regular hours and {} overtime hours worked this week.".format(total_paycheck, reg_hours, ot_hours))