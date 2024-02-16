"""2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""

class Persona:
    def __init__(self):
        self.nombre = ""
        self._saldo = 1000
        self.edad =""
        self.nacionalidad = "peruana"
        self.monto = 400

    def pedir_nombreedad(self):
        while True:
            try:
                self.nombre = input("Ingrese el nombre: ")
                break
            except (ValueError, TypeError):
                print("se ha ingresado un tipo de dato incorrecto...")

        while True:
            try:
                self.edad = int(input("Ingrese la edad: "))
                break
            except (ValueError, TypeError):
                print("se ha ingresado un tipo de dato incorrecto...")

    def cumpleaños(self):
        self.edad = self.edad + 1

    def mostrar_edad(self):
        print("la edad  de {} es {}".format(self.nombre,self.edad))



    def transferencia(self):
        print("el saldo actual de {} es {}".format(self.nombre, self._saldo))

        if self._saldo >= self.monto:
            self._saldo = self._saldo - self.monto
        else:
            print("saldo  de {} insfuciente".format(self.nombre))


class Persona2(Persona):

    def transferencia2(self):
        print("el saldo actual de {} es {}".format(self.nombre, self._saldo))

        self._saldo = self._saldo + self.monto





juan = Persona()
luis = Persona2()

juan.pedir_nombreedad()
juan.mostrar_edad()
luis.pedir_nombreedad()
luis.mostrar_edad()

juan.transferencia()
luis.transferencia2()
juan.transferencia()
luis.transferencia2()
juan.transferencia()
luis.transferencia2()



