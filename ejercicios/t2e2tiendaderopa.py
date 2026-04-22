Camiseta= 10 
Sudadera= 20.5 
Gorra= 5.5 

print("Camiseta: 10 euros")
print("Sudadera: 20.5 euros")
print("Gorra: 5.5 euros")
print("¿Qué cantidad quieres de cada artículo?")

cantidad_camisetas= int(input("Camisetas: "))
cantidad_sudaderas= int(input("Sudaderas: "))
cantidad_gorras= int(input("Gorras: "))

total_camisetas= cantidad_camisetas * Camiseta
total_sudaderas= cantidad_sudaderas * Sudadera
total_gorras= cantidad_gorras * Gorra
total_compra= total_camisetas + total_sudaderas + total_gorras

print("Total de la compra:", total_compra,)
iva= total_compra * 0.21
print("IVA: ", iva)
total_compra_con_iva= total_compra + iva
print("total con IVA:", total_compra_con_iva)




