def make_pizza(size,*toppings):
    print('the size of the pizza ' + str(size))
    for topping in toppings:
        print('- ' + topping)

make_pizza(12,'cheese')