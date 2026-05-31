"""
Shop calculator to determain total price
"""
total_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total_cost = total_cost + price_of_item
print(f"Total price for {number_of_items} items is {total_cost:0.2f}")