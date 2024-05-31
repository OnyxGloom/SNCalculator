userNumbers = []
operator = ''

# Function to ask for a number and convert it to a float
def askNumber():
    while True:
        userResponse = input("Please write a number: ")
        if isFloat(userResponse):
            return float(userResponse)
        else:
            print("Incorrect character type, please enter a number.")

# Function to check if a given input can be converted to a float
def isFloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False

# Function to ask for an operator and validate it
def askOperator():
    while True:
        userResponse = input("Please write your operator (+, -, *, /): ")
        if userResponse in ['+', '-', '*', '/']:
            return userResponse
        else:
            print("Please only use +, -, *, /.")

# Function to create and evaluate the equation
def wholeEquation(num1, operator, num2):
    equation = f"{num1} {operator} {num2}"
    try:
        result = eval(equation)
        print(f"{equation} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Main loop to perform calculations until the user chooses to stop
while True:
    userNumbers.clear()
    operator = ''
    
    num1 = askNumber()
    num2 = askNumber()
    operator = askOperator()
    
    wholeEquation(num1, operator, num2)
    
    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        break
