
#Creo función con lista meses del año
def meses():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses

# pido a la usuaria número del 1 al 12 devuelvo el mes qué es
def numero_mes():
    introducir_numero_mes = int(input("Introduce un número del 1 al 12: ")) #número del 1 al 12
    if 1 <= introducir_numero_mes <= 12: 
        meses_lista = meses()    #llamar a la lista de meses
        print(f"El mes número {introducir_numero_mes} es: {meses_lista[introducir_numero_mes - 1]}") 
        if introducir_numero_mes == 6:  #incluyo otra condición para el mes de junio(6)
         print("El mejor mes del año!")
    else: 
        print("tiene que ser un número entre 1 y 12")
    return introducir_numero_mes
numero_mes()






        







