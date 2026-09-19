# 🛒 Shopping Cart CLI

A simple console-based shopping cart application built in Python. It lets users browse products, add them to a cart, update quantities, remove items, and view a running total — all through a menu-driven terminal interface.

## Features

- 📋 View all available products with price and stock info
- ➕ Add products to the cart (with stock and quantity validation)
- ✏️ Update item quantities in the cart
- ❌ Remove items from the cart
- 🧾 View the cart with a itemized subtotal and grand total
- 🚫 Handles invalid input and out-of-stock scenarios gracefully

## Project Structure

```
shopping-cart-cli/
├── products.py   # Product catalog (list of dictionaries)
├── cart.py       # ShoppingCart class with core logic
├── main.py       # CLI menu and program entry point
└── README.md
```

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python main.py
```

## Sample Output

```
========== SHOPPING CART ==========
1. View Products
2. Add Product
3. Remove Product
4. Update Quantity
5. View Cart
6. Exit
Enter your choice: 1

========== PRODUCTS ==========
ID: 1 | Laptop | ₹55000 | Stock: 10
ID: 2 | Headphones | ₹2500 | Stock: 20
ID: 3 | T-Shirt | ₹999 | Stock: 15
ID: 4 | Shoes | ₹2999 | Stock: 8
```

## Tech Stack

- Python 3 (standard library only — no external dependencies)

## Author

Gungun Raj Sah
