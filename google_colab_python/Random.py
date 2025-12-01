'''print(f"Hola mundo!")
mensaje = "Hola mundo"
print(mensaje)
print("Cual es tu nombre?")
nombre = input()
print(f"¡Hola {nombre}!")
operacion = (((3+2)/(2*5))**2)
print(operacion)
print("Coste de la hora 50")
print("Cuantas horas trabajo hoy?")
horas_trabajadas = int(input())

if horas_trabajadas > 24:
    print("Error: El día solo tiene 24 horas.")
elif horas_trabajadas > 8:
    horas_extras = horas_trabajadas - 8
    print(f"Trabajaste {horas_extras} horas extras")
    sueldo = 8 * 50 + horas_extras * 75  # Ejemplo: horas extras pagan más
else:
    sueldo = horas_trabajadas * 50

print(f"Tu sueldo es: {sueldo}")

try:
    n = int(input("Indique un número entero positivo: "))
    if n < 1:
        print("¡Error! El número debe ser positivo.")
    else:
        suma = n * (n + 1) // 2
        print(f"La suma de los primeros {n} números naturales es: {suma}")
except ValueError:
    print("¡Debe ingresar un número entero!")

print("Ingrese su peso en kg")
peso = float(input())
print("Ingrese su estatura en metros")
estatura = float(input())
IMC = peso / estatura**2
print(f"Su IMC es: {IMC}")
import sys  # Necesario para sys.exit()

try:
    # Pedir y validar primer número
    n = int(input("Ingrese un número entero positivo: "))
    if n < 1:
        print("¡Error! El número debe ser positivo.")
        sys.exit()  # Termina el programa aquí si no es positivo

    # Pedir y validar segundo número
    n2 = int(input("Ingrese otro número entero positivo: "))
    if n2 < 1:
        print("¡Error! El número debe ser positivo.")
        sys.exit()  # Termina el programa aquí si no es positivo

    # Si ambos son válidos, calcular suma
    suma = n + n2
    print(f"La suma es: {suma}")

except ValueError:
    print("¡Debe ingresar un número entero!")
edad = int(input("Ingrese su edad:"))

if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
  
contrasena = "contrasena"
c = input("Ingrese la contrasena: ")

if c.lower() == contrasena.lower():
  print("Contraseña correcta")
else:
  print("Contraseña incorrecta")
  
entero = int(input("Ingrese un número entero: "))
entero2 = int(input("Ingrese otro número entero: "))
division = entero / entero2

if entero2 == 0:
    print("No se puede dividir entre cero")
else:
    print(f"La división de {entero} entre {entero2} es: {division}")

entero = int(input("Ingrese un número entero: "))

if entero % 2 == 0:
    print(f"{entero} es un número par")
else:
    print(f"{entero} es un número impar")
    
edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese su ingreso mensual: "))

if edad >= 16 and ingreso >= 1000:
    print("Debe tributar")
else:
    print("No debe tributar")
nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su género (H para hombre, M para mujer): ")
primera_letra_nombre = nombre[0].lower()
m = "m"
n = "n"

if primera_letra_nombre < m and genero.lower() == "m": 
  print("GURPO A")
elif primera_letra_nombre > n and genero.lower() == "h":
  print("GRUPO B")'''
'''
def generar_digitos_pi():
    # Inicialización
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            # Emitir el dígito n
            yield n
            # Actualizar variables para el próximo dígito
            q, r, t, k, n, l = (
                10 * q,
                10 * (r - n * t),
                t,
                k,
                (10 * (3 * q + r)) // t - 10 * n,
                l,
            )
        else:
            # Actualizar variables para la próxima iteración
            q, r, t, k, n, l = (
                q * k,
                (2 * q + r) * l,
                t * l,
                k + 1,
                (q * (7 * k + 2) + r * l) // (t * l),
                l + 2,
            )

# Ejemplo de uso (imprime dígitos indefinidamente)
pi_digitos = generar_digitos_pi()
contador = 0
while True:
    print(next(pi_digitos), end="", flush=True)
    contador += 1
    if contador == 1:
        print(".", end="", flush=True)  # Punto decimal después del primer dígito


with open("mensaje_uno.txt", "w", encoding = "utf-8") as f:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    f.write("Hola mundo, este es el mensaje que quiero dejar para futuras generaciones.\n")
    f.write("Espero que lo encuentren y lo disfruten.\n")
    f.write(f"Quiero hacer una mencion a {nombre} quien tiene {edad} años.\n")
    f.write("Acuerdate de tus padres y de tus amigos.\n")
    
with open("mensaje_uno.txt", "r", encoding = "utf-8") as f:
    contenido = f.read()
    print(contenido)

with open("mensaje_uno.txt", "a", encoding = "utf-8") as f:
    f.write("Es tiempo de que expreses tus sentimientos y emociones.\n")
    f.write("las personas que te aman lo necesitan.\n")
    f.write("No olvides que la vida es corta y hay que disfrutarla.\n")
    f.write(input("Escribe algo que quieras dejar en el mensaje: ") + "\n")
    
def tabla_multiplicar():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                ruta = fr"D:\Platzi\PROGRAMACION\google_colab_python\tabla-{numero}.txt"
                with open(ruta, "w", encoding="utf-8") as f:
                    for i in range(1, 11):
                        f.write(f"{numero} x {i} = {numero * i}\n")
                print(f"Tabla de multiplicar del {numero} guardada en '{ruta}'")
                return ruta  # Devuelve la ruta del archivo creado
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")

def leer_tabla_multiplicar(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
            print("Contenido de la tabla de multiplicar:\n")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
tabla_multiplicar()
archivo_no = int(input("Ingrese el número de la tabla que desea leer: "))
leer_tabla_multiplicar(fr"D:\Platzi\PROGRAMACION\google_colab_python\tabla-{archivo_no}.txt")

def leer_linea_tabla():
    try:
        n = int(input("Ingrese un número entre 1 y 10 (tabla de multiplicar): "))
        if n < 1 or n > 10:
            print("¡Error! El número debe estar entre 1 y 10.")
            return

        m = int(input("Ingrese qué línea desea ver (1 a 10): "))
        if m < 1 or m > 10:
            print("¡Error! La línea debe estar entre 1 y 10.")
            return

        ruta = fr"D:\Platzi\PROGRAMACION\google_colab_python\tabla-{n}.txt"

        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if m <= len(lineas):
            print(f"Línea {m}: {lineas[m - 1].strip()}")
        else:
            print(f"El archivo solo tiene {len(lineas)} líneas.")
    except ValueError:
        print("¡Error! Debe ingresar un número entero.")
    except FileNotFoundError:
        print(f"El archivo para la tabla del {n} no existe.")

# Llamada al programa
leer_linea_tabla()

import requests
from bs4 import BeautifulSoup # Importa BeautifulSoup

url_input = input("Ingrese la URL de la página web que desea leer: ")
url = url_input.strip()  # Elimina espacios en blanco al inicio y al final
# Verifica si la URL comienza con 'http://' o 'https://'
if not (url.startswith('http://') or url.startswith('https://')):
    print("Error: La URL debe comenzar con 'http://' o 'https://'.")
    url = input("Ingrese una URL válida: ").strip()

try:
    # 1. Obtener el código fuente HTML (como ya lo hacías)
    response = requests.get(url)
    response.raise_for_status() # Verifica si la solicitud fue exitosa

    contenido_html = response.text

    # 2. Crear un objeto BeautifulSoup
    # Le pasamos el contenido HTML y el parser a usar ('lxml' es rápido, 'html.parser' es estándar)
    # Si instalaste lxml, usa 'lxml'. Si no, usa 'html.parser'.
    try:
        soup = BeautifulSoup(contenido_html, 'lxml')
        # soup = BeautifulSoup(contenido_html, 'html.parser') # Opción si no instalaste lxml
    except Exception as e:
        print(f"Error al inicializar BeautifulSoup con lxml, intentando html.parser: {e}")
        try:
            soup = BeautifulSoup(contenido_html, 'html.parser')
        except Exception as e_parser:
            print(f"Error también con html.parser: {e_parser}")
            soup = None # No se pudo crear el objeto soup

    if soup:
        # 3. Extraer todo el texto visible de la página
        texto_pagina = soup.get_text()

        print("Solicitud exitosa.")
        print("Texto visible en la página:\n")
        print(texto_pagina[:2000]) # Imprimir los primeros 2000 caracteres del texto extraído

        # === Contar palabras ===
        palabras = texto_pagina.split()
        cantidad_palabras = len(palabras)
        print(f"\nLa página contiene aproximadamente {cantidad_palabras} palabras.")

        # Opcional: Limpiar espacios extra y saltos de línea
        # lines = texto_pagina.splitlines()
        # non_empty_lines = [line.strip() for line in lines if line.strip()]
        # cleaned_text = '\n'.join(non_empty_lines)
        # print("\nTexto visible limpio (sin líneas vacías):")
        # print(cleaned_text[:2000])

    else:
        print("No se pudo procesar el contenido HTML.")


except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al intentar leer la página {url}: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    '''
import requests
from bs4 import BeautifulSoup

url_input = input("Ingrese la URL de la página web que desea leer: ")
url = url_input.strip()  # Elimina espacios en blanco al inicio y al final

try:
    response = requests.get(url)
    response.raise_for_status() # Verifica si la solicitud fue exitosa
    contenido_html = response.text

    # Analiza el HTML
    # Usa 'lxml' si lo instalaste, si no 'html.parser'
    soup = BeautifulSoup(contenido_html, 'lxml')
    # soup = BeautifulSoup(contenido_html, 'html.parser') # Opción si no instalaste lxml

    # 1. Extraer todo el texto visible de la página
    # NOTA: Como vimos antes, get_text() extrae TODO el texto, incluyendo menús, precios, etc.
    # Si quieres buscar SOLO en el contenido del artículo, necesitarías primero
    # encontrar el contenedor del artículo con soup.find() o select_one()
    # y luego aplicar get_text() a ese contenedor específico.
    # Pero para buscar en TODO el texto visible, esto está bien.
    texto_pagina_completo = soup.get_text()
    

    print("Solicitud exitosa.")
    # Puedes comentar la siguiente línea si ya no necesitas ver todo el texto crudo
    # print("Texto visible completo de la página:\n")
    # print(texto_pagina_completo[:5000]) # Imprimir una porción o todo para inspeccionar


    # --- *** NUEVO PASO: Pedir la palabra a buscar e intentar encontrarla *** ---

    palabra_buscar_input = input("\nIngrese la palabra que desea buscar en la página: ")
    palabra_buscar = palabra_buscar_input.strip() # Limpiar espacios de la palabra buscada

    # Es MUY común querer buscar sin distinguir mayúsculas y minúsculas.
    # La forma más sencilla es convertir tanto el texto de la página como la palabra buscada a minúsculas.
    texto_para_buscar = texto_pagina_completo.lower()
    palabra_buscar_lower = palabra_buscar.lower()


    # 2. Buscar la palabra en el texto
    # Python tiene operadores y métodos muy fáciles para esto:

    # Opción A: Verificar si la palabra existe (bool)
    if palabra_buscar_lower in texto_para_buscar:
        print(f"\nLa palabra '{palabra_buscar}' FUE encontrada en el texto de la página (sin distinguir mayúsculas/minúsculas).")
    else:
        print(f"\nLa palabra '{palabra_buscar}' NO fue encontrada en el texto de la página (sin distinguir mayúsculas/minúsculas).")

    # Opción B: Contar cuántas veces aparece la palabra
    conteo = texto_para_buscar.count(palabra_buscar_lower)
    print(f"La palabra '{palabra_buscar}' aparece {conteo} veces (búsqueda sin distinguir mayúsculas/minúsculas).")


    # NOTA: La búsqueda con 'in' o 'count()' encontrará la palabra incluso si es parte de otra palabra
    # (por ejemplo, buscar "casa" encontrará "casamiento"). Si necesitas buscar solo palabras completas,
    # tendrías que usar métodos más avanzados como expresiones regulares con límites de palabra (\b)
    # o dividir el texto en una lista de palabras y buscar coincidencias exactas.
    # Por ahora, 'in' y 'count()' son los más directos.
    # --- *** NUEVO PASO: Contar palabras en el texto completo *** ---
    # Contar palabras en el texto completo
    palabras = texto_pagina_completo.split()
    cantidad_palabras = len(palabras)
    print(f"\nLa página contiene aproximadamente {cantidad_palabras} palabras.")
    # --- *** NUEVO PASO: Contar caracteres en el texto completo *** ---
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al intentar leer la página {url}: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")