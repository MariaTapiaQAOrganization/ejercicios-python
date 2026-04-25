
# Defino que numero es el ganador
def numeroganador(numero):
    if numero == 4:
        mensaje = "victoria!, has acertado!"
    elif numero < 4:
        mensaje = "derrota, no has acertado..."
    elif numero > 4:
        mensaje = "derrota, no has acertado..."
    if numero > 10:
        mensaje = "mete un número del 1 al 10"
    return mensaje

# Función para mostrar el resultado
def resultado():
    numero = int(input("Introduce un número del 1 al 10: "))
    print(numeroganador(numero))
resultado()


