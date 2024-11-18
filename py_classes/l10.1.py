products = [
    {"name": "laptop", "price": 1200, "category": "Electronics"},
    {"name": "keyboard", "price": 100, "category": "Electronics"},
    {"name": "chair", "price": 250, "category": "Forniture"},
    {"name": "desk", "price": 400, "category": "Forniture"},
    {"name": "monitor", "price": 300, "category": "Electronics"},
    {"name": "earphones", "price": 80, "category": "Electronics"},
]

products_for_lambda = products

# write a Python code to return the name of Electronics with price greater than 100

# loop over products and test if category is Electronics and price is over threshold. Put the result in a list
selection = []
for p in products:
    if p["price"] > 100 and p["category"] == "Electronics":
        selection.append(p["name"])

print(selection)

# solve the exercise by using list comprehension
l = [p["name"] for p in products if p["price"] > 100 and p["category"] == "Electronics"]

print(l)

# apply a 10% discount to all the products
# save the result in a list of dicts with same structure and edited price
discounted_products = []

for p in products:
    p["price"] = p["price"] * 0.9
    discounted_products.append(p)

# print(discounted_products)
# please note that also products have been edited and discounted
# print(products)

# alternative solution
discounted_products = products

for p in discounted_products:
    p["price"] = p["price"] * 0.9

# solution with lambda and map functions
discounted_products = list(
    map(
        lambda x: {
            "name": x["name"],
            "price": round(x["price"] * 0.9, 2),
            "category": x["category"],
        },
        products_for_lambda,
    )
)
print(products_for_lambda)
print(discounted_products)
