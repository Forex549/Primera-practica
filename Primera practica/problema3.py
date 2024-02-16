"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""


diccionario = {"nombre": "giancarlo", "apellidos": "villavicencio", "edad": 19, "dni": "123456789"}

print("1.nombre")
print("2.apellidos")
print("3.edad")
print("4.dni")

peticion = input("que desea saber?: ")


print(diccionario[peticion])


print("los valores del diccionario son: ")

for valor in list(diccionario):
    print(diccionario[valor])

diccionario["profesion"] = "Ing.Software"

del diccionario["dni"]


print("El nuevo diccionario es: {}".format(diccionario))

