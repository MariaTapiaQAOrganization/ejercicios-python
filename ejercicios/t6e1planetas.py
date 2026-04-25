
# Creo función de lista de planetas
def planetas_sistema_solar():
    return["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
    
# funcion que pide un numero del 1 al 8 y devuelve el planeta correspondiente
def numero_planeta():
    introducir_numero = int(input("Introduce un número del 1 al 8: "))
    if 1 <= introducir_numero <= 8:
        planetas = planetas_sistema_solar()
        print(f"El planeta número {introducir_numero} es: {planetas[introducir_numero - 1]}")
    else:
        print("tiene que ser un número entre 1 y 8")
numero_planeta()





    
  
    


