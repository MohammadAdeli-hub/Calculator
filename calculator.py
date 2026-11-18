
print("DISPLAY MENU\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\n5:Square Root");

number = float(input("\nEnter a number: "))

if number < 1 or number > 5:
    print("ERROR: Invalid Entry Mate.")

if number == 3:

    print("\n!!Multiplication Selected !!")
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 * num2

        print(num1, "*", num2, "=", result)

    except ValueError:
        print("ERROR: Invalid Entry Mate.")




