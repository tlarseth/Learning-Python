def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = float(input("What's x? "))
        except ValueError:
            print("That is not a number, please only enter numbers.")
        else:
            return x
main()