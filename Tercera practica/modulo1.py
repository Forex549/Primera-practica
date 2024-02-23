def crear_lista():

    lista = []

    for i in range(10):
        elemento = int(input("Ingrese un elemento: "))
        lista.append(elemento)

    print("la lista es: {} ".format(lista))
    return lista


def numeros_repetidos(lista):

    lista_no_repetidos = list(set(lista))

    return lista_no_repetidos


def ordenar(lista):

    lista_ordenada = sorted(lista)

    lista_ordenada_mayoramenor = list(reversed(lista_ordenada))

    print("la lista ordenada es: {}".format(lista_ordenada))
    print("la lista de mayor a menores: {}".format(lista_ordenada_mayoramenor))

    return lista_ordenada


def mayornumero(lista):

    lista_pares = []

    for i in lista:

        if i % 2 == 0:

            lista_pares.append(i)
        else:
            continue
    mayor = max(lista_pares)
    return mayor
