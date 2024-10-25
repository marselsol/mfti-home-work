from product import Product


class Order:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Недостаточно товара '{product.name}' на складе.")
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
        product.update_stock(-quantity)

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.products.items())

    def remove_product(self, product: Product, quantity: int):
        if product not in self.products:
            raise ValueError(f"Товар '{product.name}' отсутствует в заказе.")
        if self.products[product] < quantity:
            raise ValueError(f"Невозможно удалить {quantity} товаров '{product.name}' из заказа.")

        self.products[product] -= quantity
        product.update_stock(quantity)

        if self.products[product] == 0:
            del self.products[product]

    def return_product(self, product: Product, quantity: int):
        if product not in self.products:
            raise ValueError(f"Товар '{product.name}' отсутствует в заказе.")
        if self.products[product] < quantity:
            raise ValueError(f"Невозможно вернуть {quantity} товаров '{product.name}'.")

        self.products[product] -= quantity
        product.update_stock(quantity)

        if self.products[product] == 0:
            del self.products[product]
