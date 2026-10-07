
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self):
        if self.stock > 0:
            self.stock -= 1
        else:
            print("Product is out of stock!")

    def show_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price} kr")
        print(f"Stock: {self.stock}")

    def restock(self, amount):
        self.stock += amount


product1 = Product("Keyboard", 399, 10)

product1.show_info()
print()

product1.sell()
product1.show_info()
print()

product1.restock(5)
product1.show_info()