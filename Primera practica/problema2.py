"""2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""


lista = []

for a in range(10):
    elemento = int(input("Ingrese un elemento a la lista: "))
    lista.append(elemento)


print("la lista de elementos es: {}".format(lista))


lista2 = []

for b in lista:
    elemento2 = b**3
    lista2.append(elemento2)


print("la lista de elementos al cubo es: {}".format(lista2))


lista3 = []

for c in lista:
    elemento3 = c ** 2
    lista3.append(elemento3)


print("la lista de elementos al cuadrado es: {}".format(lista3))


lista_final = lista2 + lista3
lista_final.reverse()


print("la lista final es: {}".format(lista_final))
