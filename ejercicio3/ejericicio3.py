# Se ingresa el precioCosto del artículo
precioCosto = float(input("Ingrese el precioCosto del artículo: "))

# Se verifica la primera condición
if precioCosto < 3000:
    # Se calcula la ganancia como el 15% del precio de costo
    ganancia = precioCosto * 0.15
    # Se calcula el precio de venta
    P = precioCosto + ganancia
elif precioCosto <= 6000:
    # La ganancia se establece en $500
    ganancia = 500
    # Se calcula el precio de venta
    P = precioCosto + ganancia
else:
    # Se calcula la ganancia como el 25% del precio de costo
    ganancia = precioCosto * 0.25
    # Se calcula el precio de venta
    P = precioCosto + ganancia

# Se muestra el precio de venta
print("Precio de Venta (P):", P)