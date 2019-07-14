num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter second number: "))

# Addition
if op == "+":
    print(num1 + num2)

# Subtract
elif op == "-":
    print(num1 - num2)

# Divide
elif op == "/":
    print(num1 / num2)

# Multiply 
elif op == "*":
    print(num1 * num2)
else: print ("Error Operator")
