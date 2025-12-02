import asyncio 

async def saludo(nombre):
    await asyncio.sleep(1)
    print(f"Hola, {nombre}!")

async def saldo_banco(nombre, saldo):
    await asyncio.sleep(1)
    print(f'El saldo de {nombre} es de {saldo}')

async def main():
    await asyncio.gather(
        saludo("Alice"),
        saludo("Bob"),
        saludo("Charlie"),
        saludo("Diana"),
        saludo("Eve"),
        saludo("Frank"),
        saludo("Grace"),
        saludo("Heidi"),
        saludo("Ivan"),
        saludo("Judy"),
        saludo("Karl"),
        saludo("Leo"),
        saludo("Mallory"),
        saludo("Nina"),
        saludo("Oscar"),
        saludo("Peggy"),
        saludo("Quentin"),
        saludo("Rupert"),
        saludo("Sybil"),
        saludo("Trent"),
        saludo("Uma"),
        saludo("Victor")
    )
    print("Todos los saludos han sido enviados.")
    await asyncio.gather(
        saldo_banco("Alice", 1000),
        saldo_banco("Bob", 2000),
        saldo_banco("Charlie", 3000),
        saldo_banco("Diana", 4000),
        saldo_banco("Eve", 5000),
        saldo_banco("Frank", 6000),
        saldo_banco("Grace", 7000),
        saldo_banco("Heidi", 8000),
        saldo_banco("Ivan", 9000),
        saldo_banco("Judy", 10000),
        saldo_banco("Karl", 11000),
        saldo_banco("Leo", 12000),
    )

asyncio.run(main())