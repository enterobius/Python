# too many code duplications. Think how you can improve your code.
import sys
print('Welcome to the MegaCalculator ver. 1.0!\n\n')

A = input('Enter first operand: ')
B = input('Enter second operand: ')

operator = input("Enter operator ('+', '-', '/', '*' are allowed): ")

if operator == '+':
    C = float(A) + float(B)
elif operator == '-':
    C = float(A) - float(B)
elif operator == '/':
    C = float(A) / float(B)
elif operator == '*':
    C = float(A) * float(B)
else:
    print('Result: NaN')
    sys.exit()

print('Result:', C)
