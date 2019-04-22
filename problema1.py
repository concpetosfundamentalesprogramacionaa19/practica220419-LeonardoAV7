"""
	archivo: problema1.py
	Ejemplo de lenguaje Python
	autor; @LeonardoAV7

"""

# Pedimos los datos por teclado
costo = input ("Ingrese el costo de hora oficial: ")
horas = input ("Ingrese el número de horas trabajadas: ")

total = float(costo) * float(horas) # Calculamos el valor mensual a pagar
descuento = float(total) * 0.1 # Calculamos el descuento de 10%

print("El valor mensual a pagar es: %.2f \nEl valor de su descuento al Seguro Social es:  %.2f" % (total, descuento) )