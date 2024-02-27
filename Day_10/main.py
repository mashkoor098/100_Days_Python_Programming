from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

# operators link with functions using dictionary
oprations = {'+': add, '-': sub, '*': mul, '/': div, '%': mod}

# actual calculator func:
def calculator():
    num1 = float(input('Enter number: '))
    for symbol in oprations:
        print(symbol)
    should_continue = True
    while should_continue:

        selected_opration = input('select opration: ')
        num2 = float(input('Enter next number: '))

     # oprational_funcion contains the copy of function_call or (calling func)
        oprational_funcion = oprations[selected_opration]
        ans = oprational_funcion(num1, num2)
        print(ans)

        if input('Do you want to continue? ') == 'yes':
            num1 = ans
        else:
            should_continue = False
            if input('wants to start new calculation? ') == 'yes':
                print('::new claculation is begin:: ')
                calculator()
            else:
                should_continue = False


calculator()
