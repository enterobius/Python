print('Welcome to the MegaCalculator ver. 1.0!\n\n')

A = input('Enter first operand: ')
B = input('Enter second operand: ')

operator = input("Enter operator ('+', '-', '/', '*' are allowed): ")

if operator == '+':
    C = float(A) + float(B)
    print('Result:', C)
elif operator == '-':
    C = float(A) - float(B)
    print('Result:', C)
elif operator == '/':
    C = float(A) / float(B)
    print('Result:', C)
elif operator == '*':
    C = float(A) * float(B)
    print('Result:', C)
else:
    print('Result: NaN')