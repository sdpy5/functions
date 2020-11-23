

pizza = 'enter which pizza do you want : '
toppings = []

active = True

while active:
    pizza_name = input(pizza)
    enter_toppings = input('enter the toppings you want : ')
    toppings.append(enter_toppings)
    print(pizza_name)
    for topping in toppings:
        print(topping)