#calculator
def calculator():
    print("Welcome to the calculator!")
    print("Available operators")
    print("1. Addition(+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            operator = input("Enter symbol:")

            if operator == "+":
                result= num1 + num2
                print(f"The sum of {num1} + {num2} is:{result}")           
            elif operator == "-":
                result = num1 - num2
                print(f"The sub of {num1} - {num2} is: {result}")
            elif operator == "*":
                result = num1 * num2
                print(f"The mul of{num1} * {num2} is: {result}")
            elif operator == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The divide of{num1} / {num2} is: {result}")     
                else:
                    print("The division by zero is:undefined")
            else:
                print("Invalid operator")            
        except ValueError:
            print("Error:Invalid input. Please enter Numbers only.")
    
        choice = input("\n Do you want to perform another calculation? (yes/no): ").strip()
        if choice == "yes":
            print("Good Bye !")
            break
calculator()