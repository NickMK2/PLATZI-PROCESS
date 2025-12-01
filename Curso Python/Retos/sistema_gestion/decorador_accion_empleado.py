import datetime

def log_employee_action(func):
    def wrap(tarea, empleado_id):
        result = func(tarea, empleado_id)
        with open('registro_acciones.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - Empleado {empleado_id} realizó la tarea: {tarea}\n")
        return result
    return wrap

@log_employee_action
def realizar_tarea(tarea, empleado_id):
    # Se realiza la tarea por parte del empleado
    print(f"Empleado {empleado_id} está realizando la tarea: {tarea}")

# Ejemplo de uso
realizar_tarea("Revisar inventario", 14020)
realizar_tarea("Revisar ventas", 14021)
realizar_tarea("Recoger productos", 14022)
realizar_tarea("Atender clientes", 14023)