#from platzi_ecommerce.ventas import procesar_venta
#from platzi_ecommerce.inventario import agregar_producto, eliminar_producto
from platzi_reto.inventario.exsitencias import existencias, verificar_existencias
from platzi_reto.ventas.ordenes import gestionar_ordenes

print(existencias("Laptop", 10))
print(verificar_existencias("Laptop"))
print(gestionar_ordenes("Laptop"))

