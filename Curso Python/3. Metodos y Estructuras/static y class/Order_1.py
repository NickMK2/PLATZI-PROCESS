class Order:
    global_discount = 10  # Descuento en porcentaje
    min_amount = 20       # Monto mínimo permitido

    def __init__(self, amount):
        self.amount = amount

    @classmethod
    def update_global_discount(cls, new_discount):  # Corregido el nombre
        cls.global_discount = new_discount
    
    @staticmethod
    def validate_min_value(amount):
        if amount < Order.min_amount:
            raise ValueError(f"El monto debe ser al menos: ${Order.min_amount}")
        
    @classmethod
    def make_order(cls, order):
        # Validar el monto original
        cls.validate_min_value(order.amount)
        
        # Calcular monto con descuento
        discounted_amount = order.amount - (order.amount * (cls.global_discount / 100))
        
        # Asegurar que no sea menor que el mínimo
        final_amount = max(discounted_amount, cls.min_amount)
        
        return final_amount

# Ejemplo de uso corregido
Order.update_global_discount(50)
print("Descuento global:", Order.global_discount)  # 20
print("Monto mínimo:", Order.min_amount)           # 80

# Crear una orden de $80
order = Order(70)
print("Monto final:", Order.make_order(order))     # 80 - (80*20%) = 64 → Usa mínimo 80