# main.py

from coffee_shop.models import Coffee, Customer

def main():
    # Create Coffee
    espresso = Coffee("Espresso")

    # Create Customer
    alice = Customer("Alice")

    # Create Order
    order = alice.create_order(espresso, 5.0)

    # Display Order Information
    print(f"Customer: {alice.name}")
    print(f"Coffee: {espresso.name}")
    print(f"Order Price: {order.price}")

    # Display Coffee Orders
    print(f"Total Orders for {espresso.name}: {espresso.num_orders()}")
    print(f"Average Price of {espresso.name}: {espresso.average_price()}")

    # Display Customer Orders
    print(f"{alice.name}'s Orders: {[order.price for order in alice.orders()]}")

if __name__ == "__main__":
    main()
