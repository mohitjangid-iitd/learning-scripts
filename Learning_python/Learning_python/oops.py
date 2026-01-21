class Customer:
    all_customers = []

    def __init__(self, customer_id: int, name: str, phone: int):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def save(self):
        Customer.all_customers.append(self)
        return self

class Product:
    def __init__(self, product_id: int, category: str, name: str, price: int, available_quantity: int):
        self.product_id = product_id
        self.category = category
        self.name = name
        self.price = price
        self.available_quantity = available_quantity

    def reduce_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if self.available_quantity < quantity:
            raise ValueError(
                f"Insufficient stock for {self.name}. Available: {self.available_quantity}"
            )

        self.available_quantity -= quantity

    def restock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.available_quantity += quantity

class Order:
    order_counter = 1

    def __init__(self, customer: Customer):
        self.order_id = Order.order_counter
        Order.order_counter += 1

        self.customer = customer
        self.items = []   # list of (Product, quantity)
        self.total_price = 0

    def add_item(self, product: Product, quantity: int):
        product.reduce_stock(quantity)
        self.items.append((product, quantity))
        self.total_price += product.price * quantity

    def summary(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        for product, qty in self.items:
            print(f"- {product.name} x {qty} = {product.price * qty}")
        print(f"Total Price: {self.total_price}")

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def get_product(self, product_id: int):
        return self.products.get(product_id)

cust = Customer(1, "Mohit", 999999999).save()

p1 = Product(101, "Food", "Burger", 100, 10)
p2 = Product(102, "Food", "Pizza", 200, 5)

inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)

order = Order(cust)
order.add_item(p1, 2)
order.add_item(p2, 1)

order.summary()