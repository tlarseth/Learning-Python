# Made by Dae'Loki of the Gamer's Guild©

def calculate_net_salary(gross_salary, filing_status):
    brackets = {
        'single': [(0, 0.10), (11000, 0.12), (44725, 0.22), (95175, 0.24), (182100, 0.32), (231250, 0.35), (578125, 0.37)],
        'married': [(0, 0.10), (22000, 0.12), (89450, 0.22), (190350, 0.24), (364700, 0.32), (462500, 0.35), (731200, 0.37)]
    }

    brackets = brackets[filing_status]
    taxable_income = gross_salary
    taxes = 0

    for i in range(len(brackets) - 1, -1, -1):
        if taxable_income > brackets[i][0]:
            taxable_amount = taxable_income - brackets[i][0]
            taxes += taxable_amount * brackets[i][1]
            taxable_income -= taxable_amount

    net_salary = gross_salary - taxes
    return net_salary

def main():
    try:
        hourly_rate = int(input("Enter your hourly rate: $"))
        hours_worked = int(input("Enter the number of hours worked: "))
        filing_status = input("Enter your filing status (single or married): ").lower()

        if hourly_rate < 0 or hours_worked < 0:
            print("Please enter positive values for hourly rate and hours worked.")
            return

        regular_hours = int(min(hours_worked, 40))
        overtime_hours = int(max(0, hours_worked - 40))
        gross_salary = (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
        print(f"Your estimated gross salary before taxes is: ${gross_salary:.2f}")
        net_salary = calculate_net_salary(gross_salary, filing_status)
        print(f"Your estimated net salary after taxes is: ${net_salary:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for hourly rate and hours worked.")

if __name__ == "__main__":
    main()
