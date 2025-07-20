from inventory import Item

def main():
    """
    Main function to demonstrate the usage of the Item class.
    Creates three items and prints their details.
    """
    # Create three different items
    item1 = Item(1, "Laptop", 999.99)
    item2 = Item(2, "Mouse", 29.99)
    item3 = Item(3, "Keyboard", 59.99)
    
    # Store items in a list
    items = [item1, item2, item3]
    
    # Print header
    print("Inventory Items:")
    print("-" * 50)
    
    # Print each item's details
    for item in items:
        print(f"ID: {item.id}")
        print(f"Name: {item.name}")
        print(f"Price: ${item.price:.2f}")
        print("-" * 50)
    
    # Print just the names of all items
    print("\nAll item names:")
    print(", ".join(item.name for item in items))

if __name__ == "__main__":
    main()
