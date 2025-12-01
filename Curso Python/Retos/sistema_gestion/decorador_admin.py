def revisar_acceso(func):
    def envoltura(empleado):
        if empleado['Rol'] == 'Admin':
            return func(empleado['Nombre'])
        else:
            print(f"Lo siento {empleado['Nombre']}, no tienes acceso")
    return envoltura

@revisar_acceso
def eliminar_empleado(empleado):
    print(f"Eliminando empleado: {empleado}")
    
administrador = {'Nombre': 'Juan', 'Rol': 'Admin'}
empleado = {'Nombre': 'Pedro', 'Rol': 'Empleado'}

eliminar_empleado(administrador)
eliminar_empleado(empleado)