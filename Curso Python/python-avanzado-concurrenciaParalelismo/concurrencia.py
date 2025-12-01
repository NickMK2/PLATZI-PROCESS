import threading
import time

# Función que simula una tarea que toma tiempo
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(5)  # Simula una operación que toma 5 segundos
    print(f'Solicitud {request_id} completada')

threads = []  # Lista para almacenar los hilos

# Crear y ejecutar 5 hilos
for i in range(5):
    thread = threading.Thread(
        target=process_request,  # Función a ejecutar
        args=(i,)  # Argumentos para la función (la coma es importante para tupla)
    )
    threads.append(thread)
    thread.start()  # Inicia la ejecución del hilo

# Esperar a que todos terminen
for thread in threads:
    thread.join()  # Bloquea hasta que el hilo termine

print('Todas las solicitudes completadas')