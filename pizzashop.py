from pizza import *


# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

def print_pizza(pizza):
    """
    Print a description of a pizza, along with its price.
    """
    print(f"A {str(pizza)}")
    print("Price:", pizza.get_price())


if __name__ == "__main__":
    pizza = Pizza(PizzaSize.small)
    pizza.add_topping("mushroom")
    pizza.add_topping("tomato")
    pizza.add_topping("pinapple")
    print_pizza(pizza)

    # a plain pizza
    pizza2 = Pizza(PizzaSize.medium)
    print_pizza(pizza2)

    # pizza with only one topping
    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping("seafood")
    print_pizza(pizza3)

    # very big pizza
    pizza4 = Pizza(PizzaSize.mega)
    print_pizza(pizza4)
