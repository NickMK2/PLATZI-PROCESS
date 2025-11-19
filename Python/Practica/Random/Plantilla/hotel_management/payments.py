import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    return await asyncio.sleep(random.uniform(0.5, 2.0), f"Pago de {amount} procesado para {customer_name}")

