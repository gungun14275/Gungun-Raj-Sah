from products import products
from cart import ShoppingCart


def display_products():

    print("\n========== PRODUCTS ==========")

    for product in products:

        print(
            f"ID: {product['id']} | "
            f"{product['name']} | "
            f"₹{product['price']} | "
            f"Stock: {product['stock']}"
        )


def find_product(product_id):

    for product in products:

        if product["id"] == product_id:
            return product

    return None


def main():

    cart = ShoppingCart()

    while True:

        print("\n========== SHOPPING CART ==========")

        print("1. View Products")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Update Quantity")
        print("5. View Cart")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            display_products()

        elif choice == "2":

            display_products()

            try:
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))

                product = find_product(product_id)

                if product:
                    cart.add_item(product, quantity)
                else:
                    print("Product not found.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":

            try:
                product_id = int(input("Enter product ID: "))

                cart.remove_item(product_id)

            except ValueError:
                print("Please enter a valid product ID.")

        elif choice == "4":

            try:
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter new quantity: "))

                cart.update_quantity(product_id, quantity)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":

            cart.display_cart()

        elif choice == "6":

            print("Thank you for shopping!")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
