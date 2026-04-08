import json
import os

if os.path.exists("catalog.json"):
    with open("catalog.json", "r") as file:
        products = json.load(file)
else:
    products = ["Dresses", "Nails", "Makeup Products", "Home Decor", "Accessories", "Festival Fashion", "Amazon Affiliate links"]
for product in products:
    print(product)
print("Total produts:", len(products))
search = input("Search for a product:")
if search in products:
    print("Found it!")
else:
    print("Not in the catalog:(")    
new_product = input("Add a new product:")
products.append(new_product)
print("Updated catalog:", products)

remove_product = input("Select your product:")
if remove_product in products:
    products.remove(remove_product)
    print("Removed! Updated catalod:", products)
else:
    print("Product not found.")

with open("catalog.json", "w") as file:
    json.dump(products, file)
print("Catalog saved!")


