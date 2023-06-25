def soma(a, b):
    s = a + b
    print(int(s))


def diferenca(a, b):
    s = a - b
    print(int(s))


def multi(a, b):
    s = a * b
    print(int(s))


def dividir(a, b):
    s = a / b
    print(int(s))


a = input('valor A: ')
b = input('valor B: ')
answer = input('+ - * /: ')

if answer == '+':
    soma(a, b)
elif answer == '-':
    diferenca(a, b)
elif answer == '*':
    multi(a, b)
elif answer == '/' and b != 0:
    dividir(a, b)
else:
    print('Error! Closing the calculator!')
