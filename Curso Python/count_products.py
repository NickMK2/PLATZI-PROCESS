from collections import defaultdict

def cout_products(orders: list[str]) -> defaultdict:
    #crea un diccionario con valor por defecto 0
    
    product_count = defaultdict(int)
    for order in orders:
        product_count[order] = product_count[order] + 1
    return product_count
            
orders = ["apple", "apple", "banana", "apple", "banana", "orange", "apple", "banana","pizza","pizza","pizza"]
count = cout_products(orders)
print(count)  # defaultdict(<class 'int'>, {'apple': 4, 'banana': 3, 'orange': 1})