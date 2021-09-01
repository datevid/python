#Centra texto en imagen usando pillow

# https://www.blog.pythonlibrary.org/2021/02/02/drawing-text-on-images-with-pillow-and-python/
def centerOneLine(text, output_path):
    width, height = (400, 400)
    image = Image.new("RGB", (width, height), "grey")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        "L:\\py2021\\python\\varios\\kids.pe01\\textToImage01\\fonts\\break-snooze\\Break Snooze.ttf", size=12)
    # text = "Pillow Rocks!"
    font_width, font_height = font.getsize(text)
    new_width = (width - font_width) / 2
    new_height = (height - font_height) / 2
    draw.text((new_width, new_height), text, fill="black")
    image.save(output_path)


def centerMultilineOnlyVertical(text, output_path):
    width, height = (400, 400)
    image = Image.new("RGB", (width, height), "grey")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        "L:\\py2021\\python\\varios\\kids.pe01\\textToImage01\\fonts\\break-snooze\\Break Snooze.ttf", size=12)
    font_width, font_height = font.getsize(text)
    font_width_real, font_height1 = _widthCorrectOfTextMultiline(text, font)
    # new_width = (width - font_width) / 2
    # new_height = (height - font_height) / 2
    new_width = (width - font_width_real) / 2
    draw.multiline_text((new_width, 10), text, fill="black", align='center')
    image.save(output_path)


def _widthCorrectOfTextMultiline(text, font):
    """
    Obtiene el ancho correcto de una cadena de texto de varias lineas.
    Sucede que pillow calcula el ancho de todos los caracteres
    como si de una sola linea se tratara. 
    En la práctica es un error al dibujar caracteres de varias lineas 
    en una imagen cualquiera.
    :param text: 
    :param font: 
    :return: 
    retorna el font_width de las lineas de mayor tamaño
    """
    # split multiple text into array of lines
    textArrayLine = text.splitlines()
    textArrayLineSize = []
    for text_i in textArrayLine:
        textArrayLineSize.append(len(text_i))
        
    #cadena más larga
    largest = max(textArrayLineSize)
    #indice de la cadena más larga
    index_largest = textArrayLineSize.index(largest)
    text_largest = textArrayLine[index_largest]

    font_width, font_height = font.getsize(text_largest)
    return font_width, font_height
  
if __name__ == "__main__":

    # centerOneLine("text", "output.png")
    
    text = """Descripción del texto\nDescripción\nDescripción del texto centrado aquí"""
    centerMultilineOnlyVertical(text, "test.png")
