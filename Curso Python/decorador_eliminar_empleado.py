 
def verificar_acceso(rol_requerido):
    def decorador(func):
        def wrapper(empleado):
            if empleado['rol'] == rol_requerido:
                return func(empleado)
            else:
                print(f'No tienes permisos para eliminar a {empleado["nombre"]}, solo el rol {rol_requerido} puede hacerlo')
        return wrapper
    return decorador

def ingresar_empleado(func):
    def wrapper(empleado):
        print(f'Registrando accion para el empleado {empleado["nombre"]}')
        return func(empleado)
    return wrapper

@verificar_acceso('admin')
@ingresar_empleado
def eliminar_empleado(empleado):
    print(f'Nombre: {empleado["nombre"]} ha sido eliminado')

admin = {'nombre': 'Rodrigo', 'rol': 'admin'}
empleado = {'nombre': 'Juan', 'rol': 'empleado'}

eliminar_empleado(admin)
eliminar_empleado(empleado)
