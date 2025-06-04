# Calculator
import math

while True:
    op = input("Select your operator: (+, -, *, / , p, E to Exit) ")

    if op == "E":
        break

    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))
    
    
    if op == "+":
        result = n1 + n2
        print(result)
    elif op == "-":
        result = n1 - n2
        print(result)
    elif op == "*":
        result = n1 * n2
        print(result)
    elif op == "p":
        result = pow(n1, n2)
        print(result)
    elif op == "/":
        result = n1 / n2
        if n2 == 0:
         print("Error: Division by zero!")
    else:
        result = n1 / n2
        print(result)