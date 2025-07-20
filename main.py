from inventory import Product

def main():
    """
    Main function to demonstrate the usage of the Product class.
    Creates three products and prints their details.
    """
    # Create three different products
    item1 = Product(1, "Laptop", 999.99)
    item2 = Product(2, "Mouse", 29.99)
    item3 = Product(3, "Keyboard", 59.99)  # Fixed: Added quotes around "Keyboard"
    
    # Store items in a list
    items = [item1, item2, item3]
    
    # Print header
    print("Inventory Items:")  # Fixed: Added quotes
    print("-" * 50)
    
    # Print each item's details
    for item in items:  # Fixed: Removed slice to show all items
        print(f"ID: {item.id}")
        print(f"Name: {item.name}")
        print(f"Price: ${item.price:.2f}")
        print("-" * 50)
    
    # Print just the names of all items
    print("\nAll item names:")
    print(", ".join(item.name for item in items))

if __name__ == "__main__":
    main()
