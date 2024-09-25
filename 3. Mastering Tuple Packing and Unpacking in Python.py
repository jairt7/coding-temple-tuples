# 3. Mastering Tuple Packing and Unpacking in Python

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Kyle", "Jelly bean", 100000000000000000000000000000000000000000000000000000000000000)
]
def print_customer_data(orders):
    for order in orders:
        name, item, quantity = order
        item = item.lower()
        if quantity == 1:
            print(f"{name} ordered a(n) {item}.")
        else:
            print(f"{name} ordered {quantity} {item}s.")
# This will not work for every word, but I don't want to spend years writing out ifs for every possible plural.
# It'll still get the message across fine.

print_customer_data(orders)