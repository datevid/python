"""Adiciona comillas a los registros de un archivo
Antes:
a
b
c
Despues
'a'
'b'
'c'
"""
# Abrir el archivo en modo lectura
with open('operitDeps.txt', 'r') as file:
    # Crear una lista para almacenar las líneas con las comillas agregadas
    lines = []
    # Leer cada línea del archivo
    for line in file:

        line = line.strip()

        # Agregar comillas simples al inicio y final de la línea
        line = "'" + line + "',"
        # Agregar la línea a la lista
        lines.append(line)

# Abrir un nuevo archivo en modo escritura
with open('operitDeps_r.txt', 'w') as file:
    # Escribir cada línea en el nuevo archivo
    for line in lines:
        file.write(line)
