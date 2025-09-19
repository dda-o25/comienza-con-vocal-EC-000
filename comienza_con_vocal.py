"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
#print("Escribe una palabra:")

# Entrada
texto = input()

# Proceso
resultado = texto[0].lower() in "aeiouáéíóúü"

# Salida
if resultado:
    print(f"'{texto}' comienza con vocal")
else:
    print(f"'{texto}' no comienza con vocal")

