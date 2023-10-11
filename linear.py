def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes"]
target = "Apple"
target2= "Grapes"
result =linear_search_product(products, target2)
print(result)  # Output: [0, 3]
