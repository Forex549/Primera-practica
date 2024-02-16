"""Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""


nombre = input("Ingrese su  nombre: ")
edad = int(input("Ingrese su edad: "))


print("Los tipos de datos ingresados son {} y {} respectivamente".format(type(nombre), type(edad)))


nombre_trabajador1 = input("Ingrese el nombre del primer trabajador: ")
edad_trabajador1 = int(input("Ingrese la edad del primer trabajador: "))

nombre_trabajador2 = input("Ingrese el nombre del segundo trabajador: ")
edad_trabajador2 = int(input("Ingrese la edad del segundo trabajador: "))


lista =[nombre_trabajador1,edad_trabajador1,nombre_trabajador2,edad_trabajador2 ]


print("La suma de las edades de los trabajadores es {}".format(lista[1]+lista[3]))