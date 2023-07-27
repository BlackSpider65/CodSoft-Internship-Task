

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a , b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

def calculator():
    print("operations start:")
    print("Select the numerics number of the operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")

    while True :
        try :
            choice = int(input("Select your operation choice(1/2/3/4): "))
            if choice in (1, 2, 3, 4):
                break
            else:
                print("Invalid Choice : Please select a valid operation.")
        except ValueError :
            print("Invalid Input : Please Selact a numeric number.")
    
    while True :
        try :
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))
            break
        except ValueError :
            print("Invaild data type : Please enter a numeric data type.")

    if choice == 1 :
        result = add(num1, num2)
        operation = '+'
    elif choice == 2 :
        result = subtract(num1 , num2)
        operation = '-'
    elif choice == 3 :
        result = multiply(num1, num2)
        operation = '*'
    else :
        result = divide(num1 ,num2)
        operation = '/'

    print(f'{num1} {operation} {num2} = {result}')

if __name__ == '__main__'  :
    calculator()
