print("Function Calculator")
try:
    number = int(input("Number here:"))
    number2 = int(input("2nd Number here:"))
    print("Addition:", number + number2)
    print("Subtraction:", number - number2)
    print("Multiplication:", number * number2)
    print("Division:", number / number2)
except ValueError:
    print("Incorrect type of answer")
except ZeroDivisionError:
    print("Division by 0 is undefined")