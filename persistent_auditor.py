ORDERS_FILE = "inventory.txt"

def load_orders():
    
    orders_list = []

    try:
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    orders_list.append(line)
    except FileNotFoundError:
        pass  # No file yet — start fresh, no error

    return orders_list


def save_orders(orders):
   
    with open(ORDERS_FILE, "w") as f:
        for order in orders:
            f.write(order + "\n")


def set_order_id(orders):
   
    if not orders:
        return 1001

    last_line = orders[-1]
    last_id = int(last_line.split(",")[0].strip())
    return last_id + 1


def get_valid_quantity():
   
    user_input = input("Enter Quantity: ").strip()

    if not user_input.lstrip("-").isdigit():
        print(f"  [ERROR] '{user_input}' is not a valid integer. Entry rejected.\n")
        return -1

    quantity = int(user_input)

    if quantity < 0:
        print(f"  [ERROR] Negative quantity ({quantity}) is not allowed. Entry rejected.\n")
        return -1

    return quantity


def print_orders(orders):
    print("Current Orders:\n")
    for order in orders:
        print(order)
    print()


# Entry point
if __name__ == "__main__":
    # 1. Load persisted orders (or start empty if no file exists yet)
    orders = load_orders()

    # 2. Show what's already on record
    print_orders(orders)

    # 3. Continuous loop until 'quit' is typed as the product name
    while True:
        product_name = input("Enter Product Name(type 'quit' to end): ").strip()

        if product_name.lower() == "quit":
            break

        quantity = get_valid_quantity()

        if quantity == -1:
            continue  # rejected entry, ask again

        # 4. Build and store the new order
        new_id = set_order_id(orders)
        new_order = f"{new_id},{product_name},{quantity}"
        orders.append(new_order)

        print(f"\nNew Order Added:\n{new_order}\n")

        # 5. Write-back: persist the updated order list immediately
        save_orders(orders)
        print(f"Order successfully saved to {ORDERS_FILE}\n")

    print("Goodbye!")