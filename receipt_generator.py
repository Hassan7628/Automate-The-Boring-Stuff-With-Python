items = []
prices = []

print("\nEnter item one by one, enter 'done' to finish.")

while True:
    item = input("\nEnter the product name: ")
    if item.lower() == "done":
        break

    try:
        price = float(input("\nEnter the price of the item: "))

    except ValueError:
        print("\nEnter a numeric value")
        continue

    items.append(item)
    prices.append(price)

print("\n---- Receipt ----\n")
total = 0

for i in range(len(items)):
    print(f"{items[i]:<15} : ${prices[i]:.2f}")
    total += prices[i]

print("\n-------------------------")
print(f"Total price           ${total:.2f}")