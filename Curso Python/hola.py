a = [5,4.5/5,45,12,4845,45]
b = a
print(a)
print(b)
c = a[:]
print(c)
a.append(753951)
print(a)
print(b)
print(c)
print("-----------------------")
fila1 = [1,2,3]
fila2 = [4,5,6]
fila3 = [7,8,9]
matris = [fila1,fila2,fila3]
print(matris)
print(matris[1:500])
print(matris[2][2])
print("-----------------------")
print("Matriz de matriz")
p1 = {"Nombre" : "Jhon","Apellido" : "Cena", "Edad" : 200}
print("p1: ",p1)
values = p1.values()
Keys = p1.keys()
pairs = p1.items()
print(values)
print(Keys)
print(pairs)