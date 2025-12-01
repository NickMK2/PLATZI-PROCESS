class CuentaBancaria:
    """
    Representa una cuenta bancaria simple que mantiene un titular y un saldo,
    permite actualizar el saldo y registrar transacciones internamente.
    """

    def __init__(self, titular: str, saldo: float):
        """
        Inicializa una nueva instancia de CuentaBancaria.

        Args:
            titular (str): Nombre del propietario de la cuenta.
            saldo (float): Saldo inicial de la cuenta.
        """
        self.titular = titular
        self.saldo = saldo

    def _actualizar_saldo(self, cantidad: float) -> None:
        """
        Ajusta el saldo de la cuenta sumando la cantidad indicada.

        Este método está marcado como “_protected” para indicar que
        no es parte de la API pública, pero sigue siendo accesible.

        Args:
            cantidad (float): Monto a sumar (positivo) o restar (negativo).
        """
        self.saldo += cantidad

    def __registrar_transaccion(self) -> None:
        """
        Método privado que imprime un registro de la última transacción.

        Está precedido por doble guión bajo para impedir su acceso directo
        desde fuera de la clase (name‑mangling).
        """
        print(f"Transacción registrada — Titular: {self.titular}, Saldo: {self.saldo}")

    def mostrar_transacciones(self) -> None:
        """
        Método público para invocar el registro de transacción.

        Este es el único modo previsto de acceder a __registrar_transaccion.
        """
        self.__registrar_transaccion()


if __name__ == "__main__":
    # Ejemplos de uso
    cuenta = CuentaBancaria("Pepe", 1000)
    cuenta._actualizar_saldo(-500)
    print('Saldo:', cuenta.saldo)
    cuenta.mostrar_transacciones()
    print('-' * 60)

    cuenta = CuentaBancaria("Juana", 8000)
    cuenta._actualizar_saldo(-500)
    print('Saldo:', cuenta.saldo)
    cuenta.mostrar_transacciones()
    print('-' * 60)

    cuenta = CuentaBancaria("Camilo", 8000)
    cuenta._actualizar_saldo(50000)
    print('Saldo:', cuenta.saldo)
    cuenta.mostrar_transacciones()
    print('-' * 60)

    cuenta = CuentaBancaria("Laura", 8000)
    cuenta._actualizar_saldo(1_000_000)
    print('Saldo:', cuenta.saldo)
    cuenta.mostrar_transacciones()
