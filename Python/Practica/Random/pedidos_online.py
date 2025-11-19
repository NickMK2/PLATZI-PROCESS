import asyncio
import time
import random 
import multiprocessing

async def verificar_inventario(item):
    print(f"Verificando inventario para: {item}")
    await asyncio.sleep(random.randint(3,6))  # Simula el tiempo de verificación
    print(f"Inventario de {item} verificado.")
    return random.choice([True, False])  # Simula si el pedido fue verificado exitosamente

async def procesar_pago(orden_id):
    print(f"Procesando pago para el pedido: {orden_id}")
    await asyncio.sleep(random.randint(3,6))  # Simula el tiempo de procesamiento del pago
    print(f"Pago para el pedido {orden_id} procesado.")
    return True  # Simula si el pago fue procesado exitosamente

def calcular_total(items):
    print(f"Calculando total para el pedido: {len(items)}")
    time.sleep(random.randint(3,5))  # Simula el tiempo de cálculo
    total = sum(item['precio'] for item in items)
    print(f"Total calculado: {total}")
    return total

async def procesar_orden(orden_id, items):
    print(f"Procesando orden: {orden_id}")
    verificar_inventario_existente = [verificar_inventario(item['nombre']) for item in items]
    resultados_inventario = await asyncio.gather(*verificar_inventario_existente)
    if not all(resultados_inventario):
        print(f"Orden {orden_id} no puede ser procesada debido a inventario insuficiente.")
        return False
    
    with multiprocessing.Pool() as pool:
        total = pool.apply(calcular_total, (items,))

    pago_exitoso = await procesar_pago(orden_id)
    if pago_exitoso:
        print(f"Orden {orden_id} procesada exitosamente. Total: {total}")
        return True
    else:
        print(f"Orden {orden_id} falló en el procesamiento del pago.")
        return False
    
async def main():
    ordenes = [
        {'id': 1, 'items': [{'nombre': 'libro', 'precio': 100}, {'nombre': 'lapiz', 'precio': 200}]},
        {'id': 2, 'items': [{'nombre': 'cartulina', 'precio': 150}, {'nombre': 'borrador', 'precio': 250}]},
        {'id': 3, 'items': [{'nombre': 'esfero', 'precio': 300}, {'nombre': 'marcador', 'precio': 400}]},
        {'id': 4, 'items': [{'nombre': 'cuaderno', 'precio': 500}, {'nombre': 'regla', 'precio': 600}]},
        {'id': 5, 'items': [{'nombre': 'calculadora', 'precio': 700}, {'nombre': 'goma', 'precio': 800}]},
        {'id': 6, 'items': [{'nombre': 'tijeras', 'precio': 900}, {'nombre': 'pegamento', 'precio': 1000}]},
        {'id': 7, 'items': [{'nombre': 'pintura', 'precio': 1100}, {'nombre': 'brocha', 'precio': 1200}]},
        {'id': 8, 'items': [{'nombre': 'papel', 'precio': 1300}, {'nombre': 'sobre', 'precio': 1400}]},
        {'id': 9, 'items': [{'nombre': 'carpeta', 'precio': 1500}, {'nombre': 'archivador', 'precio': 1600}]},
        {'id': 10, 'items': [{'nombre': 'marcador permanente', 'precio': 1700}, {'nombre': 'rotulador', 'precio': 1800}]}
    ]
    
    tareas = [procesar_orden(orden['id'], orden['items']) for orden in ordenes]
    resultados = await asyncio.gather(*tareas)
    
    print("Todas las órdenes han sido procesadas.")
    print(f"Resultados: {resultados}")

if __name__ == "__main__":
    asyncio.run(main()) 