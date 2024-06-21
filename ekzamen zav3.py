class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def display_info(self):
        print(f"Продукт: {self.name}, Ціна: {self.price:.2f} грн")
        print(f"Загальна кількість створених продуктів: {Product.count}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Гарантійний термін: {self.warranty_period} міс.")

class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Розмір: {self.size}")

if __name__ == "__main__":
    laptop = ElectronicProduct("Ноутбук", 45000, 12)
    t_shirt = ClothingProduct("Футболка", 299, "L")

    print("Інформація про ноутбук:")
    laptop.display_info()
    print()

    print("Інформація про футболку:")
    t_shirt.display_info()
    print()
    
    print(f"Загальна кількість створених продуктів: {Product.count}")

