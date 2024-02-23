"""1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número par de la lista (lista
del ítem 2), retornar este valor e imprimirlo por consola."""

import modulo1

lista1 = modulo1.crear_lista()

lista2 = (modulo1.numeros_repetidos(lista1))
print("la lita sin repeticiones es: {} ".format(lista2))
lista3 = modulo1.ordenar(lista2)
print("el maayor par de la lista es:{}".format(modulo1.mayornumero(lista3)))
