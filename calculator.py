
while True:
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    op = input("Operation:")

    if op in ('+','-','*','/','%'):
        if op == '+':
            print(num1, '+', num2, '=', num1+num2)
        elif op == '-':
            print(num1, '-', num2, '=', num1-num2)
        elif op == '*':
            print(num1, '*', num2, '=', num1*num2)
        elif op == '/':
            print(num1, '/', num2, '=', num1/num2)
        elif op == '%':
            print(num1, '%', num2, '=', num1%num2)

        next = input("Continue..? (yes/no)")
        if next == 'no':
            break

    else:
        print("Check the input")
