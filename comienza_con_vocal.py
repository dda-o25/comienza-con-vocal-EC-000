"""
El propósito de este código es de comporbar si cualquier palabra escrita en el inicia con una vocal o no
Eduardo Caleb Castillo Llanas 18/Sep/25
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

