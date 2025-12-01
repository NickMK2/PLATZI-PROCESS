import random

j1 = 0
j2 = 0
resta = 0

print("PIEDRA🪨 = 1, PAPEL📜 = 2, TIJERA✂️ = 3")

j1 = int(input("Jugador 1, elige: "))
j2 = random.randint(1, 3)

resta = j1 - j2

# Validación de entrada (opcional)
while j1 not in [1, 2, 3]:
    print("Opción inválida. Elige 1, 2 o 3.")
    j1 = int(input("Jugador 1 eligio: "))

print(f"El computador o jugador2 eligio: {j2}")

if j1 == j2:
    print("EMPATE")
elif resta == -2 or resta == 1:
    print("Gana J1")
elif resta == -1 or resta == 2:
    print("Gana J2 o PC")
