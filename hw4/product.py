class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        if self.stock + quantity < 0:
            raise ValueError("Недостаточно товара на складе для обновления.")
        self.stock += quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"
