import asyncio

async def descargar_archivo(archivo, tiempo_espera):
    print(f'Descargando {archivo}...')
    await asyncio.sleep(tiempo_espera)
    print(f'{archivo} descargado.') 

async def main():
    await asyncio.gather(
        descargar_archivo("archivo1.txt", 3),
        descargar_archivo("archivo2.txt", 2),
        descargar_archivo("archivo3.txt", 1),
        descargar_archivo("archivo4.txt", 4),
        descargar_archivo("archivo5.txt", 2),
        descargar_archivo("archivo6.txt", 3),
        descargar_archivo("archivo7.txt", 5),
        )
    print("Todos los archivos han sido descargados.")

asyncio.run(main())