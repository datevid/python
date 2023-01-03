def detectar_lineas_duplicadas(nombre_archivo):
  # Abrir el archivo en modo de lectura
  with open(nombre_archivo, "r") as archivo:
    # Crear un diccionario para almacenar las líneas leídas
    lineas = {}
    # Iterar sobre cada línea del archivo
    for linea in archivo:
      # Eliminar los espacios en blanco al principio y al final de la línea
      linea = linea.strip()
      # Saltear las líneas vacías
      if not linea:
        continue
      # Convertir la línea a minúsculas
      linea_min = linea.lower()
      # Si la línea ya existe en el diccionario, se trata de una línea duplicada
      if linea_min in lineas:
        print("Línea duplicada encontrada: ", linea)
      else:
        # Agregar la línea al diccionario
        lineas[linea_min] = True

# Usar la función para detectar líneas duplicadas en un archivo de texto
detectar_lineas_duplicadas("archivo.txt")
