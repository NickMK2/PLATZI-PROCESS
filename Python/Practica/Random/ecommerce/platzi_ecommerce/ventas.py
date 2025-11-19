def procesar_venta(nombre_producto, cantidad):
    """
    Procesa una venta de un producto.

    Args:
        nombre_producto (str): Nombre del producto vendido.
        cantidad (int): Cantidad vendida del producto.

    Returns:
        str: Mensaje de éxito.
    """
    return f"Venta procesada: {cantidad} unidades de '{nombre_producto}' vendidas."
