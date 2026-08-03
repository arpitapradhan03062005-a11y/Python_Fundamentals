class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        return total

    
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 1000, 2)
product3 = Product("Keyboard", 2000, 1)

cart = [product1, product2, product3]

total = 0

for product in cart:
    print(product.name, ":", product.total_price())
    total += product.total_price()

print("Total cart value:", total)