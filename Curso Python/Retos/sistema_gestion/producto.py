class Producto:
    """
    Representa un producto en el inventario.

    Cada producto tiene un nombre, un precio y una cantidad. Se implementan propiedades
    para acceder, modificar y eliminar estos atributos, aplicando validaciones en los setters.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa una nueva instancia de Producto.

        Args:
            nombre (str): El nombre del producto.
            precio (float o int): El precio del producto.
            cantidad (int): La cantidad disponible del producto.
        """
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def __str__(self):
        """
        Retorna una cadena que representa el producto.

        Se utiliza getattr para manejar el caso en que alguno de los atributos haya sido eliminado.
        
        Returns:
            str: Cadena en el formato "Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}".
        """
        nombre = getattr(self, "_nombre", "Eliminado")
        precio = getattr(self, "_precio", 0)
        cantidad = getattr(self, "_cantidad", 0)
        return f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}"

    @property
    def nombre(self):
        """
        Propiedad para obtener el nombre del producto.

        Returns:
            str: El nombre del producto.
        """
        return self._nombre

    @property
    def precio(self):
        """
        Propiedad para obtener el precio del producto.

        Returns:
            float o int: El precio del producto.
        """
        return self._precio

    @property
    def cantidad(self):
        """
        Propiedad para obtener la cantidad disponible del producto.

        Returns:
            int: La cantidad disponible.
        """
        return self._cantidad

    @nombre.setter
    def nombre(self, nombre):
        """
        Setter para actualizar el nombre del producto.

        Args:
            nombre (str): El nuevo nombre del producto.
        """
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        """
        Setter para actualizar el precio del producto.

        Valida que el precio no sea negativo.

        Args:
            precio (float o int): El nuevo precio del producto.

        Raises:
            ValueError: Si el precio es negativo.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    @cantidad.setter
    def cantidad(self, cantidad):
        """
        Setter para actualizar la cantidad disponible del producto.

        Valida que la cantidad no sea negativa.

        Args:
            cantidad (int): La nueva cantidad disponible.

        Raises:
            ValueError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    @nombre.deleter
    def nombre(self):
        """
        Deleter para eliminar el atributo nombre del producto.
        """
        del self._nombre

    @precio.deleter
    def precio(self):
        """
        Deleter para eliminar el atributo precio del producto.
        """
        del self._precio

    @cantidad.deleter
    def cantidad(self):
        """
        Deleter para eliminar el atributo cantidad del producto.
        """
        del self._cantidad


# Lista global que representa el inventario
inventario = []


def agregar_producto(producto):
    """
    Agrega un producto al inventario.

    Args:
        producto (Producto): El objeto producto a agregar.
    """
    inventario.append(producto)


def eliminar_producto_de_inventario(producto):
    """
    Elimina un producto del inventario, si existe.

    Args:
        producto (Producto): El objeto producto a eliminar.
    """
    if producto in inventario:
        inventario.remove(producto)


# --- Ejemplo de uso del sistema de inventario ---
if __name__ == "__main__":
    # Crear instancias de Producto
    producto = Producto("Laptop", 1500, 10)
    producto2 = Producto("Mouse", 50, 100)
    producto3 = Producto("Teclado", 80, 50)
    producto4 = Producto("Monitor", 300, 20)
    producto5 = Producto("Impresora", 200, 15)

    print("-" * 20)

    # Agregar productos al inventario
    agregar_producto(producto)
    agregar_producto(producto2)
    agregar_producto(producto3)
    agregar_producto(producto4)
    agregar_producto(producto5)

    # Mostrar inventario completo
    print("Inventario:")
    for prod in inventario:
        print(prod)
    print("-" * 20)

    # Modificar atributos de algunos productos
    producto.nombre = "Laptop Gaming"
    producto.precio = 2000
    producto.cantidad = 5

    producto2.nombre = "Mouse Inalámbrico"
    producto2.precio = 60
    producto2.cantidad = 80
    
    producto4.nombre = "Monitor 4K"
    producto4.precio = -400
    producto4.cantidad = 10
    
    producto5.nombre = "Impresora Multifuncional"
    producto5.precio = 250
    producto5.cantidad = -12

    # Eliminar un producto del inventario
    eliminar_producto_de_inventario(producto)

    # Mostrar inventario actualizado
    print("Inventario actualizado:")
    for prod in inventario:
        print(prod)
    print("-" * 20)

    # Mostrar información del producto eliminado
    print(f"Información del producto eliminado: {producto}")