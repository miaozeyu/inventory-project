class Product:
    """
    A class to represent an item in the inventory.
    
    Attributes:
        id (int): The unique identifier for the item
        name (str): The name of the item
        price (float): The price of the item in dollars
    """
    
    def __init__(self, item_id: int, name: str, price: float):
        """
        Initialize a new Item instance.
        
        Args:
            item_id: The unique identifier for the item
            name: The name of the item
            price: The price of the item in dollars
        """
        self.id = item_id
        self.name = name
        self.price = price
        
    def __str__(self) -> str:
        """Return a string representation of the item."""
        return f"Product(id={self.id}, name='{self.name}', price={self.price:.2f})"
    
    def __repr__(self) -> str:
        """Return the official string representation of the item."""
        return f"Product({self.id}, '{self.name}', {self.price})"
