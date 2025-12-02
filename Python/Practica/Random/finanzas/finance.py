def calcular_balance_mes(ingresos, gastos):
    # Calcula el balance mensual restando los gastos de los ingresos
    balance = ingresos - gastos
    return balance

def mes_rentable(balance):
    # Determina si el mes es rentable 
    if balance > 0:
        return True
    else:
        return False

