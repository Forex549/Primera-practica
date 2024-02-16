"""3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""

def ingresar_datos():
    while True:
        try:
            dato1 = int(input("Ingrese el primer dato: "))
            dato2 = int(input("Ingrese el segundo dato: "))
            return dato1, dato2
        except ValueError:
            print(" Ingrese valore numerico...")

def division_entrecero():

    while True:
        try:
            resultado = dato1 / dato2
            return resultado
        except ZeroDivisionError:
            print("No se puede dividir entre cero. Intente nuevamente.")
            for i in dato1,dato2:

            ingresar_datos()

def suma_datos_incorrectos():
    while True:
        try:

        except ValueError:



