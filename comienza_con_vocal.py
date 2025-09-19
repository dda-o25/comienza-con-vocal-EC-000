"""
Inserta el encabezado aquí y escribe tu código abajo
"""
# Declaraciones
print("Escribe una palabra:")

# Entradas
texto = input()
# Proceso
resultado = (texto[0].lower() in "aeiou")

# Salidas
if resultado == True:
    print(texto,"inicia con vocal")

else:
    print(texto,"no inicia con vocal")
