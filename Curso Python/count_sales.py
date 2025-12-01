from collections import Counter

def count_sales(products: list[str]) -> Counter:
    
    # Se utiliza Counter para saber cuantos productos se han vendido de cada tipo   
    return Counter(products)

sales = ["smartphone", "smartphone", "tablet", "smartphone", "tablet",
         "laptop", "smartphone", "tablet","headphones","headphones","headphones","RJ45","RJ45","RJ45"]

count = count_sales(sales)  
print(count)  # Counter({'smartphone': 4, 'tablet': 3, 'headphones': 3, 'laptop': 1})