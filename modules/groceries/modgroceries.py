# grocery_module.py

# Dictionary of grocery items with prices
grocery_items = {
    'Rice': 40,
    'Wheat': 35,
    'Sugar': 45,
    'Oil': 120,
    'Milk': 30,
    'Eggs': 6
}

def show_items():
    print("Available Items:")
    for item, price in grocery_items.items():
        print(f"- {item}: ₹{price} per unit")

def add_to_cart(cart, item, quantity):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

def calculate_bill(cart):
    print("\n----- BILL -----")
    total = 0
    for item, qty in cart.items():
        price = grocery_items[item]
        item_total = price * qty
        total += item_total
        print(f"{item} - {qty} unit(s) x ₹{price} = ₹{item_total:.2f}")
    print("----------------")
    print(f"Total Amount: ₹{total:.2f}")
    return total
