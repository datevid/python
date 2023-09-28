import pandas as pd


def convertir_texto_a_lista(texto):
    """
  Convierte texto a una lista, eliminando los espacios en blanco y los espacios adicionales.

  Args:
    texto: El texto a convertir.

  Returns:
    Una lista con los datos convertidos.
  """
    # Convertir los datos
    df = pd.DataFrame({
        "datos": texto.split("\n")
    })

    # Eliminar los espacios en blanco
    df["datos"] = df["datos"].str.replace(r"\s+", " ")

    # Eliminar los espacios adicionales al principio y al final
    df["datos"] = df["datos"].str.strip()
    datosList = df["datos"].tolist()

    # Eliminar los arrays vacíos
    datosList = [
        linea for linea in datosList if linea
    ]

    return datosList;


# Definir los datos
datos = """
linea 1
linea 2
línea 3
"""

datosList = convertir_texto_a_lista(datos)

# Imprimir los datos convertidos
print(datosList)
