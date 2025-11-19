import reports

reporte_ventas = reports.generar_reporte_ventas('enero', 10000)
reporte_gastos = reports.generar_reporte_gastos('enero', 5000)
reporte_utilidades = reports.generar_reporte_utilidades('enero', 5000)
reporte_inventario = reports.generar_reporte_inventario('enero', 200)
reporte_clientes = reports.generar_reporte_clientes('enero', 150)

# Imprimir los reportes generados
print("Reportes Generados:")
print(reporte_ventas)
print(reporte_gastos)
print(reporte_utilidades)
print(reporte_inventario)
print(reporte_clientes)