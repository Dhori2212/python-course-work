# main.py

import modgroceries as gm

def main():
    print("Welcome to the Grocery Store!\n")
    gm.show_items()

    cart = {}

    while True:
        choice = input("\nEnter the item to buy (or type 'done' to finish): ").capitalize()
        if choice == 'Done':
            break
        if choice in gm.grocery_items:
            try:
                quantity = float(input(f"Enter quantity of {choice}: "))
                gm.add_to_cart(cart, choice, quantity)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Item not available.")

    gm.calculate_bill(cart)
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
