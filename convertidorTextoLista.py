import pandas as pd

# Definir los datos
datos = """
linea 1
linea 2
línea 3
"""

# Convertir los datos
df = pd.DataFrame({
    "datos": datos.split("\n")
})

# Eliminar los espacios en blanco
df["datos"] = df["datos"].str.replace(r"\s+", " ")

# Eliminar los espacios adicionales al principio y al final
df["datos"] = df["datos"].str.strip()
datosList=df["datos"].tolist()

# Eliminar los arrays vacíos
datosList = [
    linea for linea in datosList if linea
]

# Imprimir los datos convertidos
print(datosList)

"""
output:
['linea 1', 'linea 2', 'línea 3']
"""
