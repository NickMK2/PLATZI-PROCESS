def agregar_producto(nombre_producto, existencia):
    """
    Agrega un producto al inventario.

    Args:
        nombre_producto (str): Nombre del producto.
        existencia (int): Cantidad de existencia del producto.

    Returns:
        str: Mensaje de éxito.
    """
    return f"Producto '{nombre_producto}' agregado con {existencia} unidades."

def eliminar_producto(nombre_producto):
    """
    Elimina un producto del inventario.

    Args:
        nombre_producto (str): Nombre del producto a eliminar.

    Returns:
        str: Mensaje de éxito.
    """
    return f"Producto '{nombre_producto}' eliminado del inventario."