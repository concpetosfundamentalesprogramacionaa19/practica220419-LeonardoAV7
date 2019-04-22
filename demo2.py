import sys
"""
	archivo: demo2.py
	Ejemplo de lenguaje Python
	autor; @LeonardoAV7

"""
nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

suma = int(valor1) + int(valor2)  # aqui realizco la suma de variables
multiplicacion = int(valor1) * int(valor2) #aqui realizo la multiplicacion

print("variable argv[0]: %s" % nombre_archivo)
print("La suma es: %d" % suma)
print("La multipliacion es: %d" % multiplicacion)
