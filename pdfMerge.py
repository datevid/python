import os
import sys
import PyPDF2

def mergePdf(filenames,outputFile):
    # Crea una instancia de PdfFileMerger
    merger = PyPDF2.PdfMerger()

    # Agrega cada archivo a la instancia de PdfFileMerger
    for filename in filenames:
        merger.append(open(filename, 'rb'))

    # Abre el archivo resultante en modo escritura
    with open(outputFile, 'wb') as fout:
        merger.write(fout)


def mergePdfDirectory(input_dir, output_file):
    """
    Une todos los pdf que se encuentran en un directorio
    """
    # Abrir el archivo PDF resultante
    output_pdf = open(output_file, 'wb')

    # Crear una lista con todos los archivos PDF del directorio
    pdf_files = []
    for file in os.listdir(input_dir):
        if file.endswith('.pdf'):
            pdf_files.append(file)

    # Crear un objeto "PDF merge" y una lista vacía para almacenar los archivos PDF
    pdf_merger = PyPDF2.PdfMerger()
    pdfs = []

    # Abrir cada archivo PDF y agregarlo al objeto "PDF merge" y a la lista de archivos PDF
    for file in pdf_files:
        with open(f'{input_dir}/{file}', 'rb') as pdf:
            pdf_merger.append(pdf)
            pdfs.append(pdf)

    # Escribir el contenido del objeto "PDF merge" en el archivo PDF resultante y cerrar ambos archivos
    pdf_merger.write(output_pdf)
    output_pdf.close()
    for pdf in pdfs:
        pdf.close()


# Obtiene la lista de nombres de archivo de la lista de strings

filenames = [
            'docsAbeja/A-2.Cover.pdf', 
            'docsAbeja/A-2.pdf', 
            'docsAbeja/A-2.CoverBack.pdf', 
            ]
mergePdf(filenames,'resultado.pdf')
#mergePdfDirectory('docsAbeja','salida.pdf')
