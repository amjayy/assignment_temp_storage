def cake_pops_available(inventory, orders):
    print(f"You have {inventory} cake pops available!")
    print(f"You have {orders} orders to fufill today!")
    print("Get to work!")
    print("Or you won't have a job!\n")

print("We can just the function numbers directly:")
cake_pops_available( 500, 225)

print("Use variables from the script to keep track.:")
inventory = 483
orders = 120

cake_pops_available(inventory, orders)

print("Add them up in style:")
cake_pops_available(200+ 30 - 45, 100 - 58)

print("What are you looking at? Get over there and start combining!:")
cake_pops_available(inventory + 225, orders + 75)

print("How about some good old fashioned multiplication.:")
orders = 49
inventory = orders * 2
cake_pops_available(orders + inventory, orders)

print("Let's try this method...or you're fired!:")
orders_today = input(orders)
available_inventory = input(inventory)
cake_pops_available(inventory, orders)

print("Or how about this?")
cake_pops_availble = input()
orders = 200
if cake_pops_available != inventory:
    print(orders)



    


