import finance

balance = finance.calcular_balance_mes(2999, 3000)
rentable = finance.mes_rentable(balance)

print(f"El balance mensual es: {balance}")
print(f"¿El mes es rentable? {'Sí' if rentable else 'No'}")
