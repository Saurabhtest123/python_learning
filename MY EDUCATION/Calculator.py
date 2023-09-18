# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function to run the calculator
def main():
    while True:
        # Display menu
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        
        # Take user input
        user_input = input(": ")
        
        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            # Get numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform the requested operation
            if user_input == "add":
                result = add(num1, num2)
            elif user_input == "subtract":
                result = subtract(num1, num2)
            elif user_input == "multiply":
                result = multiply(num1, num2)
            elif user_input == "divide":
                result = divide(num1, num2)
            
            # Display the result
            print("Result:", result)
        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    main()
