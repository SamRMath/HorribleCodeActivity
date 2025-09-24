# Function to add 2 numbers
def add(x, y):
    return x+y
# Function to subtract 2 numbers
def sub(x, y):
    return x-y
# Function to multiply 2 numbers
def mul(x, y):
    return x*y
# Function to divide 2 numbers
def div(x, y):
    if y == 0:
        return "Error: Cannot Divide by Zero"
    return x/y

# Calculator function based on user input
def calculator():
    print("Calculator")
    print("Enter first number: ")
    num1 = int(input())
    print("Enter operator: ")
    operator = input()
    print("Enter second number: ")
    num2 = int(input())

    result = 0

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = sub(num1, num2)
    elif operator == "*":
        result = mul(num1, num2)
    elif operator == "/":
        result = div(num1, num2)
    else:
        print("Invalid operator")

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
