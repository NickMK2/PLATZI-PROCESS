from collections import defaultdict

class Producto:
    """
    Clase que representa un producto en el sistema de gestión.
    
    Atributos:
        nombre (str): Nombre del producto.
        precio (int o float): Precio del producto.
        stock (int): Cantidad en stock del producto.
        estatus (str): Estado del pedido asociado al producto.
                       Valores comunes: 'PENDING', 'SHIPPED', 'DELIVERED', 'ON_HOLD', 'CANCELLED'.
    """
    def __init__(self, nombre, precio, stock, estatus):
        """
        Inicializa una instancia de Producto.

        Args:
            nombre (str): Nombre del producto.
            precio (int o float): Precio del producto.
            stock (int): Cantidad en stock.
            estatus (str): Estado del pedido.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.estatus = estatus

    def __str__(self):
        """
        Retorna una cadena que representa el producto de forma legible.
        
        Returns:
            str: Representación del producto con su nombre, precio, stock y estatus.
        """
        return f'Nombre: {self.nombre} Precio: {self.precio} Stock: {self.stock} Estatus: {self.estatus}'

def sistema_gestion():
    """
    Crea y retorna la lista inicial de productos disponibles en el sistema.
    
    Returns:
        list[Producto]: Lista con instancias de la clase Producto.
    """
    productos = [
        Producto('Smartphone', 100, 10, 'PENDING'),
        Producto('Tablet', 200, 20, 'SHIPPED'),
        Producto('Laptop', 300, 30, 'DELIVERED'),
        Producto('Smartwatch', 400, 40, 'PENDING'),
        Producto('Headphones', 500, 50, 'ON_HOLD'),
        Producto('Speaker', 600, 60, 'CANCELLED'),
        Producto('Mouse', 700, 70, 'PENDING'),
        Producto('Keyboard', 800, 80, 'SHIPPED'),
        Producto('Monitor', 900, 90, 'DELIVERED'),
        Producto('Printer', 1000, 100, 'PENDING')
    ]
    return productos

def check_order_status(status):
    """
    Retorna un mensaje descriptivo basado en el estatus del pedido.
    
    Args:
        status (str): Estado del pedido.
    
    Returns:
        str: Mensaje descriptivo del estado.
    """
    if status == 'PENDING':
        return "La orden está pendiente"
    elif status == 'SHIPPED':
        return "La orden ha sido enviada"
    elif status == 'DELIVERED':
        return "La orden ha sido entregada"
    elif status == 'ON_HOLD':
        return "La orden está en espera"
    elif status == 'CANCELLED':
        return "La orden ha sido cancelada"
    else:
        return "Orden no encontrada"

def get_all_products(productos):
    """
    Retorna todos los productos de la lista proporcionada.
    
    Args:
        productos (list[Producto]): Lista de productos.
    
    Returns:
        list[Producto]: Una lista que contiene cada producto de la lista de entrada.
        
    Nota:
        Se utiliza una comprensión de listas para recorrer cada elemento de 'productos'.
        La variable 'p' en la comprensión representa cada elemento (producto) en la lista.
    """
    return [p for p in productos]

def get_products_by_status(productos, status):
    """
    Filtra y retorna los productos que coincidan con el estatus dado.

    Args:
        productos (list[Producto]): Lista de productos.
        status (str): El estatus a filtrar (por ejemplo, 'PENDING', 'SHIPPED', etc.).
    
    Returns:
        list[Producto]: Lista de productos cuyo atributo 'estatus' coincide (sin distinguir mayúsculas/minúsculas) con el valor de 'status'.
    """
    return [p for p in productos if p.estatus.upper() == status.upper()]

def find_product_by_name(productos, name):
    """
    Busca y retorna el primer producto cuyo nombre coincida exactamente (ignorando mayúsculas/minúsculas) con el valor proporcionado.

    Args:
        productos (list[Producto]): Lista de productos.
        name (str): Nombre del producto a buscar.
    
    Returns:
        Producto: El producto encontrado, o None si no se encuentra ninguno.
    """
    for p in productos:
        if p.nombre.lower() == name.lower():
            return p
    return None

def update_product_status(productos, name, new_status):
    """
    Actualiza el estatus de un producto buscado por nombre.

    Args:
        productos (list[Producto]): Lista de productos.
        name (str): Nombre del producto a actualizar.
        new_status (str): Nuevo estatus que se asignará al producto.
    
    Returns:
        bool: True si la actualización fue exitosa, False si el producto no se encontró.
    """
    producto = find_product_by_name(productos, name)
    if producto:
        producto.estatus = new_status.upper()
        return True
    return False

def group_products_by_status(productos):
    """
    Agrupa los productos por su estatus utilizando un defaultdict.

    Args:
        productos (list[Producto]): Lista de productos.
    
    Returns:
        defaultdict: Un diccionario en el que la clave es el estatus y el valor es una lista de productos que tienen ese estatus.
    """
    grouped = defaultdict(list)
    for p in productos:
        grouped[p.estatus].append(p)
    return grouped

def menu():
    """
    Función principal que presenta un menú interactivo para gestionar productos.
    
    Opciones del menú:
        1. Ver todos los productos.
        2. Filtrar productos por estatus.
        3. Buscar un producto por nombre.
        4. Actualizar el estatus de un producto.
        5. Agrupar productos por estatus.
        6. Salir.
    
    El usuario ingresa la opción deseada, y se ejecuta la función correspondiente.
    """
    productos = sistema_gestion()  # Obtiene la lista inicial de productos.
    while True:
        print("\n--- Menú de Gestión de Pedidos ---")
        print("1. Ver todos los productos")
        print("2. Filtrar productos por estatus")
        print("3. Buscar producto por nombre")
        print("4. Actualizar estatus de un producto")
        print("5. Agrupar productos por estatus")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción 1: Mostrar todos los productos con un formato alineado.
            print("\nTodos los productos:")
            print(f"{'Producto':<15} || {'Precio':<10} || {'Stock':<10} || {'Estatus':<15}")
            print("-" * 55)
            for p in get_all_products(productos):
                # Se imprime cada producto utilizando los atributos con un ancho fijo.
                print(f"{p.nombre:<15}    {p.precio:<10}    {p.stock:<10}     {p.estatus:<15}")
        elif opcion == "2":
            # Opción 2: Filtrar productos por estatus.
            status = input("Ingrese el estatus a filtrar (PENDING, SHIPPED, DELIVERED, ON_HOLD, CANCELLED): ")
            filtrados = get_products_by_status(productos, status)
            if filtrados:
                print(f"\nProductos con estatus {status.upper()}:")
                for p in filtrados:
                    print(p)
            else:
                print("No se encontraron productos con ese estatus.")
        elif opcion == "3":
            # Opción 3: Buscar un producto por nombre.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = find_product_by_name(productos, nombre)
            if producto:
                print(f"\nProducto encontrado:\n{producto}")
                print(check_order_status(producto.estatus))
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            # Opción 4: Actualizar el estatus de un producto.
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nuevo_estatus = input("Ingrese el nuevo estatus (PENDING, SHIPPED, DELIVERED, ON_HOLD, CANCELLED): ")
            if update_product_status(productos, nombre, nuevo_estatus):
                print("Estatus actualizado correctamente.")
            else:
                print("No se encontró el producto.")
        elif opcion == "5":
            # Opción 5: Agrupar productos por estatus y mostrarlos.
            agrupados = group_products_by_status(productos)
            for estatus, lista in agrupados.items():
                print(f"\nEstatus: {estatus}")
                for p in lista:
                    print(p)
        elif opcion == "6":
            # Opción 6: Salir del sistema.
            print("Saliendo del sistema...")
            break
        else:
            print("Debe seleccionar una opción válida del menu.")

if __name__ == "__main__":
    menu()
