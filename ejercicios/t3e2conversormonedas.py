def cantidad_en_euros():
    cantidad_euros = float(input("Cantidad en euros: "))
    return cantidad_euros

def convertir_a_dolares(cantidad_euros):
    cambio = 1.1 
    cantidad_dolares = cantidad_euros * cambio
    return cantidad_dolares

def convertir_a_libras(cantidad_euros):
    cambio = 0.87
    cantidad_libras = cantidad_euros * cambio
    return cantidad_libras

print("Introduce cantidad en euros:")
cantidad_euros = cantidad_en_euros()
print("dólares:", convertir_a_dolares(cantidad_euros))
print("libras:", convertir_a_libras(cantidad_euros))



