from order import Order
from product import Product


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f"Товар: {product.name}, Цена: {product.price}, Остаток: {product.stock}")

    def create_order(self):
        return Order()
