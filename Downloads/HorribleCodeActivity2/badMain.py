#+
def add(x, y):
    x = x + y
    return x
#-
def sub(x, y):
    x = x - y
    return x
#*
def mul(x, y):
    x = x * y
    return x
#/
def div(x, y):
    if y == 0:
        return "error: cannot divide by 0" #why would you try this (sorry if too mean)
    else:
        x = x / y
        return x

#da calculator
def calculator():
    whattheinputwas = 0
    print("calculator")
    print("enter first number: ")
    whattheinputwas = int(input())
    num1 = whattheinputwas
    print("enter operator: ")
    whattheinputwas = input()
    operator = whattheinputwas
    print("enter second number: ")
    whattheinputwas = int(input())
    num2 = whattheinputwas

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
        print("invalid operator") #bruh

    print(f"result: {result}")

if __name__ == "__main__":
    calculator()
