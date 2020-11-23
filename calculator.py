def add():
    number1 = int(input('enter the number >> '))
    number2 = int(input('enter the number >> '))
    addition = number1 + number2
    return addition

def sub():
    number1 = int(input('enter the number >> '))
    number2 = int(input('enter the number >> '))
    subtraction = number1 - number2
    return subtraction

def mul():
    number1 = int(input('enter the number >> '))
    number2 = int(input('enter the number >> '))
    multiplication = number1 * number2
    return multiplication

def div():
    number1 = int(input('enter the number >> '))
    number2 = int(input('enter the number >> '))
    division = number1 // number2
    return division

def formula():
    a = int(input('a = '))
    b = int(input('b = '))
    formulas = a**2 + 2*a*b + b**2
    return formulas


user_input = '''tell us your option type add sub mul or div\n 
enter quit to quit the calculator  >>  '''

active = True

while active:
    user = input(user_input)
    if user == 'add':
        addi = add()
        print(addi)

    elif user == 'sub':
        subtractions = sub()
        print(subtractions)
    elif user == 'mul':
        multiplications = mul()
        print(multiplications)
    elif user == 'div':
        divisions = div()
        print(divisions)
    elif user == 'formula':
        form = formula()
        print(form)
    elif user == 'quit':
        active = False

