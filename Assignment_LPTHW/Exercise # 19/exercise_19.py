def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f" You have{boxes_of_crackers} boxes of crackers!")
    print("Man!That's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our own script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can eve do math inside to:")
cheese_and_crackers(10+ 20, 5+6)

print("And we can combine two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
