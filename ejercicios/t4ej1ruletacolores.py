
# Defino la función, recibe un color y me devuelve un mensaje según el color
def ruletacolor(color):
    if (color== "rojo"):
        mensaje = "El rojo es un color de pasión y energía"
    elif (color== "verde"):
        mensaje = "El verde es un color de esperanza y crecimiento"
    elif (color== "azul"):
        mensaje = "El azul es un color de calma y serenidad"
    elif (color== "amarillo"):
        mensaje = "El amarillo es un color de felicidad y optimismo"
    elif (color== "morado"):
        mensaje = "El morado es un color de sabiduría y creatividad"
    else:
        mensaje = "Color no válido"    
    return mensaje

#Función para mostrar el resultado
def resultado():
    color = input("Elige un color: rojo, verde, azul, amarillo o morado: ") 
    print(ruletacolor(color))
resultado()

