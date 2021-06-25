# Write a Python program that takes the content of a dictionary and converts it into a list of lists.
# Each nested list should contain a key as the first element and its corresponding value as the second element.
# Print the final list of lists.

product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

new_product_info = []

for key, value in product_info.items():
    new_product_info.append([key, value])

print(new_product_info)
