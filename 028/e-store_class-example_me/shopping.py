

class ShoppingCart:

    def __init__(self):
        self.products = []
        self.active = False

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total_cost(self):
        total = 0
        for product in self.products:
            total += product.price
