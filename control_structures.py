def number_classification():
    while True:
        user_input = input("Enter a number (or 'exit' to stop): ")
        
        if user_input.lower() == "exit":
            print("Program terminated.")
            break

        try:
            num = float(user_input)
            if num > 0:
                print(f"{num} is a positive number.")
            elif num < 0:
                print(f"{num} is a negative number.")
            else:
                print("The number is zero.")
        except ValueError:
            print("Invalid, Please enter a valid number.")

number_classification()
