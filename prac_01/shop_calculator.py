MAXIMUM_VALUE = 100
DISCOUNT_RATE = 0.1
total_price = 0


number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = float(input("Price of items: "))
    total_price += price_of_items
if total_price > MAXIMUM_VALUE:
    total_price *= (1-DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")


