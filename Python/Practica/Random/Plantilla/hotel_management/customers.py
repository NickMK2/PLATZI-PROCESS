class Customer:
    def __init__():
        pass

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        """Agrega un nuevo cliente al sistema."""
        if customer.id in self.customers:
            raise ValueError("El cliente ya existe.")
        self.customers[customer.id] = customer

    def get_customer(self, customer_id):
        """Obtiene la información de un cliente por ID."""
        return self.customers.get(customer_id, None)