import os
import PyPDF2

def splitPdfAllPages(pdf_path, output_dir):
    # Abre el archivo PDF
    with open(pdf_path, 'rb') as file:
        # Crea un objeto PdfReader
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Itera por cada página en la lista de páginas
        for page in range(total_pages):
            # Crea un objeto PdfWriter
            pdf_writer = PyPDF2.PdfWriter()
            # Agrega la página actual al objeto PdfWriter
            #pdf_writer.addPage(pdf_reader.getPage(page))
            pdf_writer.add_page(pdf_reader.pages[page])

            # Crea el nombre del archivo para la página actual
            output_filename = 'pagina-{}.pdf'.format(page+1)
            output_path = os.path.join(output_dir, output_filename)

            # Crea el archivo para la página actual
            with open(output_path, 'wb') as output:
                pdf_writer.write(output)

    # Cierra el archivo PDF original
    file.close()

def split_pdf(pdf_path, pages, output_dir):
    # Abre el archivo PDF
    with open(pdf_path, 'rb') as file:
        # Crea un objeto PdfReader
        pdf_reader = PyPDF2.PdfReader(file)

        # Itera por cada página en la lista de páginas
        for page in pages:
            # Crea un objeto PdfWriter
            pdf_writer = PyPDF2.PdfWriter()
            # Agrega la página actual al objeto PdfWriter
            #pdf_writer.addPage(pdf_reader.getPage(page))
            pdf_writer.add_page(pdf_reader.pages[page])

            # Crea el nombre del archivo para la página actual
            output_filename = 'pagina-{}.pdf'.format(page+1)
            output_path = os.path.join(output_dir, output_filename)

            # Crea el archivo para la página actual
            with open(output_path, 'wb') as output:
                pdf_writer.write(output)

    # Cierra el archivo PDF original
    file.close()

def split_pdf_range(pdf_path, from_page, to_page, output_dir):
    # Abre el archivo PDF
    with open(pdf_path, 'rb') as file:
        # Crea un objeto PdfReader
        pdf_reader = PyPDF2.PdfReader(file)

        # Itera por cada página en el rango de páginas
        for page in range(from_page, to_page+1):
            # Crea un objeto PdfWriter
            pdf_writer = PyPDF2.PdfWriter()
            # Agrega la página actual al objeto PdfWriter
            pdf_writer.add_page(pdf_reader.pages[page])

            # Crea el nombre del archivo para la página actual
            output_filename = 'pagina-{}.pdf'.format(page+1)
            output_path = os.path.join(output_dir, output_filename)

            # Crea el archivo para la página actual
            with open(output_path, 'wb') as output:
                pdf_writer.write(output)

# Ejemplo de uso
#split_pdf('A-2-withcovert.pdf', [0, 2, 3], '')
#split_pdf_range('A-2-withcovert.pdf', 1, 32, '')
splitPdfAllPages('A-2-withcovert.pdf', '')
