
# Pido al usuario cuántas notas va a meter
def cantidad_notas():
    total_notas = int (input("Introduce el número de notas: "))
    return total_notas

# pido al usuario las notas y se guardan en una lista de notas
def solicitar_notas (total):
    notas = []
    for i in range(total):
        nota =(float (input("Introduce la nota: ")))
        notas.append(nota)
    return notas

# calculo la nota media usando la lista de notas y la cantidad
def calcular_media(notas):
    cantidad = len(notas)
    suma = sum(notas)
    media = suma / cantidad
    return media

# imrpimo la nota final con un mensaje según la nota
def resultado_final():
    total = cantidad_notas()
    notas = solicitar_notas(total)
    media = calcular_media(notas)       
    print("la nota media es:", media, "buen trabajo" if media >= 5 else "sigue estudiando")

resultado_final()

