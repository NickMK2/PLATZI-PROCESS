import asyncio
import time
import random
import multiprocessing

async def verificar_inventario(item):
    print(f"Verificando inventario para {item}...")
    await asyncio.sleep(random.randint(3,6))
    print(f"Inventario verificado para {item}.")
    return random.choice([True, False])

async def procesar_pedido(orden_id):
    print(f"Procesando pago para la orden {orden_id}...")
    await asyncio.sleep(random.randint(3,6))
    print(f"Pedido {orden_id} procesado.")
    return True

def calcular_total(items):
    print(f"Calculando el costo total para {len(items)} articulos...")
    time.sleep(5)
    total = sum(item['precio'] for item in items)
    print(f"Costo total calculado: {total}")
    return total

async def procesar_orden(orden_id, items):
    print(f"Procesando orden {orden_id}...")
    verificacion_inventario = [verificar_inventario(item['nombre']) for item in items]
    resultados_inventario = await asyncio.gather(*verificacion_inventario)
    if not all(resultados_inventario):
        print(f"Orden {orden_id} no puede ser procesada debido a inventario insuficiente.")

    with multiprocessing.Pool() as pool:
        total = pool.apply(calcular_total, (items,))
    
    resultado_pago = await procesar_pedido(orden_id)
    if resultado_pago:
        print(f"Orden {orden_id} procesada con éxito. Total: {total}")
    else:
        print(f"Error al procesar la orden {orden_id}.")

async def main():
    ordenes = [
        {'id': 1, 'items': [{'nombre': 'mouse', 'precio': 100}, {'nombre': 'celular', 'precio': 200}]},
        {'id': 2, 'items': [{'nombre': 'teclado', 'precio': 150}, {'nombre': 'pc', 'precio': 250}]},
        {'id': 3, 'items': [{'nombre': 'parlante', 'precio': 300}, {'nombre': 'portatil', 'precio': 400}]}
    ]
    
    tareas = [procesar_orden(orden['id'], orden['items']) for orden in ordenes]
    await asyncio.gather(*tareas)

if __name__ == "__main__":
    asyncio.run(main())