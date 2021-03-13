def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print("\nСоздание " + str(size) + "-дюймовой пицци со следующими начинками:")
    for topping in toppings:
        print("- " + topping)


# make_pizza(46, 'колбаса')
