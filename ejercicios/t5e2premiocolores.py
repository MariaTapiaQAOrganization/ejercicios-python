
# la función pide un color en 5 intentos si es azul tiene premio
def introducir_colores():
    colores = []
    for i in range(5):
        color = input(f"Introduce el color tienes 5 intentos, intento {i + 1}: ")
        colores.append(color)
        if color == "azul":
            mensaje = "premio conseguido!"
            print(mensaje)
            break
        else:
            mensaje = "prueba otro color"
            print(mensaje)  
    return colores
introducir_colores()
