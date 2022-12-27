import os
import sys
from PyPDF2 import PdfMerger

# PdfFileMerger está deprecado, se ćambió por PdfMerger
# Crea una instancia de PdfFileMerger
merger = PdfMerger()

# Obtiene la lista de nombres de archivo de la lista de strings
filenames = [
            'file01.pdf','file02.pdf',
            ]

# Agrega cada archivo a la instancia de PdfFileMerger
for filename in filenames:
    merger.append(open(filename, 'rb'))

# Abre el archivo resultante en modo escritura
with open('resultado.pdf', 'wb') as fout:
    merger.write(fout)
