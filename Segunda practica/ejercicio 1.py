"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""


import datetime

class Persona:
    def __init__(self):
        self.nombre = ""
        self.saldo = 1000
        self.edad =""
        self.nacionalidad = "peruana"

    def pedir_nombreedad(self):
        while True:
            try:
                self.nombre = input("Ingrese el nombre: ")
                break
            except (ValueError, TypeError, NameError):
                print("se ha ingresado un tipo de dato incorrecto...")

        while True:
            try:
                self.edad = int(input("Ingrese la edad: "))
                break
            except (ValueError):
                print("se ha ingresado un tipo de dato incorrecto...")

    def cumpleaños(self):
        self.edad = self.edad + 1

    def mostrar_edad(self):
        print("la edad aumentada de {} es {}".format(self.nombre,self.edad))

    def tiempo(self):
        fecha_actual = datetime.datetime.now()
        hora = fecha_actual.hour
        minuto = fecha_actual.minute
        return "la fecha, hora y minuto en que se registro a la persona es: {}, {} ,{}".format(fecha_actual, hora, minuto)

persona_1 = Persona()
persona_2 = Persona()

persona_1.pedir_nombreedad()
persona_1.cumpleaños()
persona_1.cumpleaños()
persona_1.mostrar_edad()
print(persona_1.tiempo())

persona_2.pedir_nombreedad()
persona_2.cumpleaños()
persona_2.cumpleaños()
persona_2.mostrar_edad()
print(persona_2.tiempo())






