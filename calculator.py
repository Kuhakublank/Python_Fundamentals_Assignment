def calc():
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        if y != 0: 
            return x / y 
        else:
            print("Error: Division by zero")

    def mod(x, y):
        if y != 0:
            return x % y
        else: 
            print("Error: Division by zero")

    while True:
        choice = input("Enter choice (1/2/3/4/5) or 'exit' to quit: ")
        
        if choice.lower() == 'exit':
            print("Calculator closed !! ")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {add(n1, n2)}")
                elif choice == '2':
                    print(f"Result: {sub(n1, n2)}")
                elif choice == '3':
                    print(f"Result: {mul(n1, n2)}")
                elif choice == '4':
                    print(f"Result: {div(n1, n2)}")
                elif choice == '5':
                    print(f"Result: {mod(n1, n2)}")
            except ValueError:
                print("Invalid input. Please enter number values.")
        else:
            print("Invalid choice. Please select a valid option.")

calc()
