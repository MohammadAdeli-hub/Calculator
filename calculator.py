



number = int(input("Enter a number: "))
if number == 3:

    print("Multiplication Selected")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 * num2

        print(num1, "*", num2, "=", result)

    except ValueError:
        print("Invalid Entry Mate.")


