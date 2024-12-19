def calculate_net_salary(gross_salary, filing_status):
    if filing_status == "single":
        brackets = [
            (0, 0.10), (11000, 0.12), (44725, 0.22), (95175, 0.24),
            (182100, 0.32), (231250, 0.35), (578125, 0.37)
        ]
    else:
        brackets = [
            (0, 0.10), (22000, 0.12), (89450, 0.22), (190350, 0.24),
            (364700, 0.32), (462500, 0.35), (731200, 0.37)
        ]

    taxable_income = gross_salary
    taxes = 0

    for i in reversed(range(len(brackets))):
        if taxable_income > brackets[i][0]:
            taxable_amount = taxable_income - brackets[i][0]
            taxes += taxable_amount * brackets[i][1]
            taxable_income -= taxable_amount

    return gross_salary - taxes

def main():
    while True:
        try:
            hourly_rate = float(input("Enter your hourly rate: $"))
            hours_worked = float(input("Enter the number of hours worked: "))
            filing_status = input("Enter your filing status (single or married): ").lower()

            if hourly_rate < 0 or hours_worked < 0:
                print("Please enter positive values for hourly rate and hours worked.")
                continue

            if filing_status not in ["single", "married"]:
                raise ValueError("Invalid filing status. Please enter 'single' or 'married'.")

            break
        except ValueError as e:
            print(e)

    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)
    gross_salary = (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
    print(f"Your estimated gross salary before taxes is: ${gross_salary:.2f}")

    net_salary = calculate_net_salary(gross_salary, filing_status)
    print(f"Your estimated net salary after taxes is: ${net_salary:.2f}")

if __name__ == "__main__":
    main()
