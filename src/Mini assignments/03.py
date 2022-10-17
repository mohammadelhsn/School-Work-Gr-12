def price(toppings):
    return toppings * 0.75 + 8.00


print("Welcome to Python Pizza!")

pizzas = 0

while pizzas != 3:
    try:
        toppings = int(input(f"How many toppings on pizza #{pizzas+1}? "))
        print(
            f"For a pizza with {toppings} topping(s), the total would be: ${price(toppings)}"
        )
        pizzas = pizzas + 1
    except Exception as e:
        print(e)
        continue
