class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}'

def productos_descuento(*productos, **kwargs):
    # Extraemos el valor de 'porcentaje' del diccionario kwargs.
    # Si no se pasa 'porcentaje', se asume 0.
    porcentaje = kwargs.get('porcentaje', 0)
    
    for producto in productos:
        if porcentaje == 0:
            print(f'No hay descuento para {producto.nombre}, precio: {producto.precio}')
        else:
            precio_final = producto.precio - (producto.precio * porcentaje)
            print(f'El precio de {producto.nombre} con descuento {porcentaje} es: {precio_final}')

lista_productos = [
    Producto('Camisa', 500),
    Producto('Pantalon', 1000),
    Producto('Zapatos', 1500),
    Producto('Gorra', 200),
    Producto('Cinturon', 300),
    Producto('Calcetines', 1123654.5)
]

# Ejemplos de uso:
print('Ejemplos de uso:')
productos_descuento(*lista_productos, porcentaje=0)      # Sin descuento
print('-'*60)
productos_descuento(*lista_productos, porcentaje=0.1)    # Aplica un 10% de descuento
print('-'*60)
productos_descuento(*lista_productos, porcentaje = 0.5)  # Aplica un 50%                  # Sin descuento
print('-'*60)