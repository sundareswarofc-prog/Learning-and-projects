cart = [
    {"name": "Laptop", "price": 50000, "quantity": 1},
    {"name": "Mouse", "price": 800, "quantity": 2},
    {"name": "Keyboard", "price": 1500, "quantity": 1},
    {"name": "Monitor", "price": 12000, "quantity": 2},
    {"name": "Headphones", "price": 2000, "quantity": 1}
]

most_expensive=max(cart,key=lambda x:x["price"])
highest_cart_value=max(cart,key=lambda x:x["price"]*x['quantity'])
multiple_quantity_products=max(cart,key=lambda x:x["quantity"])


for x in cart:
    print(f"{x['name']}      | rs{x['price']} | qty: {x['quantity']} | Total: {x['quantity']*x['price']}")


print(f"Most Expensive: {most_expensive["name"]} - {most_expensive['price']}")
print(f"Highest cart value: {highest_cart_value["name"]} - {highest_cart_value['price']}")
print(f"Multiple quantity products: {multiple_quantity_products["quantity"]}")