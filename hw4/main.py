from product import Product
from store import Store

store = Store()

product1 = Product("Ноутбук", 1000, 5)
product2 = Product("Смартфон", 500, 10)

store.add_product(product1)
store.add_product(product2)

store.list_products()

order = store.create_order()

order.add_product(product1, 2)
order.add_product(product2, 3)

total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

store.list_products()
