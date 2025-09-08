a = float(input("Enter first number: "))  # input
b = float(input("Enter second number: ")) # input

print("1.Add  2.Subtract  3.Multiply  4.Divide")  
op = int(input("Choose: "))  # choice

if op == 1:  # add
    print("Result =", a + b)
elif op == 2:  # sub
    print("Result =", a - b)
elif op == 3:  # mul
    print("Result =", a * b)
elif op == 4:  # div
    if b != 0:  # check
        print("Result =", a / b)
    else:  # error
        print("Error: Division by zero")
else:  # invalid
    print("Invalid choice")
