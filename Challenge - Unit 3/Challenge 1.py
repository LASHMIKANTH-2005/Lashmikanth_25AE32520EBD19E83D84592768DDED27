#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes","cherry","Apple"]
target= "Apple"
result = linear_search_product(products, target)
print(result)  # Output will be [0, 3,6] because "Apple" is found at indices 0 ,3 and 6.
target2="mango"
result = linear_search_product(products, target2)
print(result)# output will be empty list[] because "mango" is not found in the list of products