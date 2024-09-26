def main():
    x, op, y = input("Expression: ").split(" ")
    x = float()
    y = float()
    match op:
        case "+":
            print(f"{x + y:.1f}")
        case "-":
            print(f"{x - y:.1f}")
        case "*":
            print(f"{x * y:.1f}")
        case "/":
            print(f"{x / y:.1f}")
main()

