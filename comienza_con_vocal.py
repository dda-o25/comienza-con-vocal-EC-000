"""
Inserta el encabezado aquí y escribe tu código abajo
"""
# Declaraciones
#print("Escribe una palabra:")

# Entradas
texto = input()
# Proceso
resultado = (texto[0].lower() in "aeiouáéíóúü")

# Salidas
if resultado == True:
    print(texto,"comienza con vocal")

else:
    print(texto,"no comienza con vocal")
