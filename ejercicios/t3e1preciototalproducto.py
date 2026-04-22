def datos_compra():
    nombre_producto = input("nombre del producto: ")
    precio_unidad = float(input("precio por unidad: "))
    cantidad = int(input("cantidad: "))
    descuento = float(input("descuento (%) : "))
    Iva = float(input("IVA (%) : "))
    return nombre_producto, precio_unidad, cantidad, descuento, Iva


def total_compra(precio_unidad,cantidad,descuento,Iva):
    precio_total = precio_unidad * cantidad
    descuento_total = precio_total * (descuento / 100)
    precio_con_descuento = precio_total - descuento_total
    iva_total = precio_con_descuento * (Iva / 100)
    precio_final = precio_con_descuento + iva_total
    return precio_final

print("Introduce los datos de la compra:")
nombre_producto, precio_unidad, cantidad, descuento, Iva = datos_compra()
print("Total: ", total_compra(precio_unidad,cantidad,descuento,Iva))    