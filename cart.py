class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):

        product_id = product["id"]

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > product["stock"]:
            print("Not enough stock available.")
            return

        if product_id in self.items:
            new_quantity = self.items[product_id]["quantity"] + quantity

            if new_quantity > product["stock"]:
                print("Cannot add more than available stock.")
                return

            self.items[product_id]["quantity"] = new_quantity

        else:
            self.items[product_id] = {
                "product": product,
                "quantity": quantity
            }

        print(f"{product['name']} added to cart.")

    def remove_item(self, product_id):

        if product_id in self.items:
            product_name = self.items[product_id]["product"]["name"]

            del self.items[product_id]

            print(f"{product_name} removed from cart.")

        else:
            print("Product is not in the cart.")

    def update_quantity(self, product_id, quantity):

        if product_id not in self.items:
            print("Product is not in the cart.")
            return

        product = self.items[product_id]["product"]

        if quantity <= 0:
            self.remove_item(product_id)
            return

        if quantity > product["stock"]:
            print("Not enough stock available.")
            return

        self.items[product_id]["quantity"] = quantity

        print("Quantity updated.")

    def calculate_total(self):

        total = 0

        for item in self.items.values():

            product = item["product"]
            quantity = item["quantity"]

            total += product["price"] * quantity

        return total

    def display_cart(self):

        if not self.items:
            print("\nYour cart is empty.")
            return

        print("\n========== YOUR CART ==========")

        for item in self.items.values():

            product = item["product"]
            quantity = item["quantity"]

            subtotal = product["price"] * quantity

            print(
                f"{product['name']} | "
                f"₹{product['price']} x {quantity} = ₹{subtotal}"
            )

        print("-------------------------------")
        print(f"Total: ₹{self.calculate_total()}")
