class CuentaBancaria: 
    
    def __init__(self, cliente_cuenta, balance):
        self.cliente_cuenta = cliente_cuenta
        self.balance = balance
        self.activa = True
        
    def deposito(self, monto):
        if self.activa:
            self.balance += monto
            print(f"Se depositaron {monto}. Saldo actual: {self.balance}")
        else:
            print("La cuenta está inactiva y no se puede depositar")

    def retiro(self, monto):
        if self.activa:
            if self.balance >= monto:  # Corregido: El saldo debe ser mayor o igual al monto a retirar
                self.balance -= monto
                print(f"Se retiraron {monto}. Saldo actual: {self.balance}")
            else:
                print("No puede exceder el saldo de su cuenta")
        else:
            print("La cuenta está inactiva y no se puede retirar")

    def desactivar_cuenta(self):
        self.activa = False      
        print("Se desactivó la cuenta")                             

    def activar_cuenta(self):
        self.activa = True      
        print("Se activó la cuenta")
    
    def __str__(self):
        estado = "Activa" if self.activa else "Inactiva"
        return f"Cuenta de {self.cliente_cuenta}, Saldo: {self.balance}, Estado: {estado}"                             

# Pruebas
cuenta1 = CuentaBancaria("Ana", 5000000)
cuenta2 = CuentaBancaria("Ramiro", 50000000)

cuenta1.deposito(500000)
cuenta2.deposito(700000000)

# Imprimir cuentas
print(cuenta1)
print(cuenta2)

# Desactivar y probar depositar en cuenta desactivada
cuenta1.desactivar_cuenta()
cuenta1.deposito(300000000)

# Imprimir cuenta desactivada
print(cuenta1)
