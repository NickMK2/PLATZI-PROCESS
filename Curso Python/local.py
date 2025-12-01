x = 100

def local_function():
    x = 10
    print(f"El valor de la variable es {x}")
    print(f"direccion memoria local function " , id(x))

def show_global():
    global x
    x = 500
    print(f"El valor de la variable global es {x}")
    print(f"direccion memoria global function " , id(x))
    
local_function()
show_global()
print(id(x))
