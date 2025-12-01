import os
import json
from decimal import Decimal, getcontext
from time import time

# ================ CONFIGURACIÓN FINAL ================
DIRECTORIO = r"D:\Platzi\PROGRAMACION\PI"
CHECKPOINT_FILE = os.path.join(DIRECTORIO, "pi_checkpoint.json")
OUTPUT_FILE = os.path.join(DIRECTORIO, "pi.txt")
PRECISION = 2000  # Número de dígitos objetivo por "porción"

# Ajustamos el contexto Decimal
getcontext().prec = PRECISION + 1000  # Precisión extendida para cálculos intermedios
getcontext().Emax = 10_000_000         # Límite exponencial aumentado para evitar overflow
getcontext().Emin = -2_000_000         # Mínimo exponente

os.makedirs(DIRECTORIO, exist_ok=True)

# ================ FUNCIONES DE CONTROL ================
def guardar_progreso(pi_aproximado, iteracion, tiempo):
    """Guarda el progreso en un archivo checkpoint (JSON)."""
    datos = {
        'pi': str(pi_aproximado),
        'iteracion': iteracion,
        'tiempo': tiempo,
        'precision': PRECISION  # Clave esencial añadida
    }
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(datos, f)

def cargar_progreso():
    """Carga el progreso desde el archivo checkpoint, o retorna valores iniciales si no existe."""
    if not os.path.exists(CHECKPOINT_FILE):
        return Decimal(0), 0, 0.0
    
    with open(CHECKPOINT_FILE, 'r') as f:
        try:
            data = json.load(f)
            if data.get('precision', 0) != PRECISION:
                raise ValueError("La precisión ha cambiado. Borra el archivo de checkpoint.")
            return Decimal(data['pi']), data['iteracion'], data['tiempo']
        except Exception:
            os.remove(CHECKPOINT_FILE)
            return Decimal(0), 0, 0.0

# ================ ALGORITMO DE CHUDNOVSKY ================
def calcular_pi():
    """
    Calcula los dígitos de π de forma indefinida usando el algoritmo de Chudnovsky,
    guardando el progreso y los dígitos en archivos externos para poder reanudar el cálculo.
    
    Para pausar la ejecución, presiona Ctrl+C y el progreso se guardará en el checkpoint.
    """
    C = Decimal(426880) * Decimal(10005).sqrt()
    
    # Inicialización de variables (usando Decimal)
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(-262537412640768000)
    suma = L
    K = Decimal(6)
    
    iteracion = 0
    pi_actual, iteracion, tiempo_acum = cargar_progreso()
    start = time()

    try:
        while True:
            # Cálculo del término actual
            term = (K**3 - 16*K) / Decimal((iteracion + 1)**3)
            M *= term
            
            L += Decimal(545140134)
            X *= Decimal(-262537412640768000)  # Conversión a Decimal explícita
            suma += (M * L) / X
            K += Decimal(12)
            iteracion += 1

            if iteracion % 5 == 0:
                pi_actual = C / suma
                with open(OUTPUT_FILE, 'a') as f:
                    f.write(f"\nIteración {iteracion} - Tiempo: {time() - start + tiempo_acum:.2f}s\n")
                    # Guardamos solo la porción de dígitos definida por PRECISION
                    f.write(str(pi_actual)[:PRECISION] + "\n")
                guardar_progreso(pi_actual, iteracion, time() - start + tiempo_acum)

    except KeyboardInterrupt:
        guardar_progreso(pi_actual, iteracion, time() - start + tiempo_acum)
        print(f"\n🔥 Proceso interrumpido. Dígitos guardados: {len(str(pi_actual)) - 2}")

# ================ EJECUCIÓN PRINCIPAL ================
if __name__ == "__main__":
    # Si deseas reanudar el cálculo sin borrar el progreso previo, comenta (o elimina) las siguientes líneas:
    # if os.path.exists(CHECKPOINT_FILE):
    #     os.remove(CHECKPOINT_FILE)
    # if os.path.exists(OUTPUT_FILE):
    #     os.remove(OUTPUT_FILE)
    
    print(f"🚀 Iniciando cálculo de π con objetivo de {PRECISION} dígitos por porción (se guardará el progreso).")
    calcular_pi()
