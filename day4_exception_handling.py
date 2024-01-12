try:
    x = float(input("Enter a number "))
    y = float(input("Enter a number "))
    operator = input("Enter an operator ")
    if operator == '+':
        print(x + y)
    elif operator == '-':
        print(x - y)
    elif operator == '*':
        print(x * y)
    elif operator == '/':
        print(x / y)
    else:
        print("Enter a valid operator")
except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Denominator can't be zero")





