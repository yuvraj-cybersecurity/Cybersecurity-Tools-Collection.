def calculator():
    print("--- Advanced Calculator & Converter ---")
    print("1. Add\n2. Subtract\n3. KM to Miles Converter")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a + b}")
    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a - b}")
    elif choice == '3':
        km = float(input("Enter KM: "))
        print(f"Miles: {km * 0.621371}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    calculator()
