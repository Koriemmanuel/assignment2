operator = input('pick your operator (- * + /): ')
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
else:
    print('invalid operator')

