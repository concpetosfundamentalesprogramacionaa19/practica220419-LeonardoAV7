"""
	archivo: problema1.py
	Ejemplo de lenguaje Python
	autor; @LeonardoAV7

"""

# Pedimos los datos por teclado
x = input ("Ingrese la variable x: ")
y = input ("Ingrese la variable y: ")
z = input ("Ingrese la variable z: ")

# Realizamos la operacion definida de "m"
m = (float(x)+(float(y)/float(z)))/(float(x)-(float(y)/float(z)))

print ("El valor de m, en base a las variables:\nx = %.1f \n\ty = %.1f\
	\n\t\tz = %.1f\nda como resultado:\n\t\t\tm = %.2f\n"
	 % (float(x), float(y), float(z), m ) )