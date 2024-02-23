"""- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados usando el decorador implementado
con un mínimo tres ejemplos."""

def decorador_sumar_elementos(func):

    def funfinal(*args, **kwargs):
        resultado = func(*args, **kwargs)
        suma = sum(args) + sum(kwargs.values())
        print("la suma de elemtnos es:{}".format(suma))
        return resultado
    return funfinal


def multiplicacion(**kwargs):

    resultado = 1
    for valor in kwargs.values():
        resultado = resultado * valor

    return resultado

