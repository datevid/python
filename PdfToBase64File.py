import base64
import os
import sys


def PdfToBase64File(filePathInput, filePathOutput):
    """
    Convierte el archivo pdf en base64encode y el resultado lo guarda en  un archivo txt.
    Also can use the variable encodedBytes
    :param filePathInput: full path de entrada
    :param filePathOutput: full path de salida donde retorna B64encode
    """
    if os.path.isfile(filePathInput):
        print('File exists: ' + str(os.path.isfile(filePathInput)))
    else:
        print('File not found!')
        sys.exit()

    # read file
    in_file = open(filePathInput, "rb")  # opening for [r]eading as [b]inary
    data = in_file.read()  # data have file in memory
    in_file.close()

    # print(data)
    encodedBytes = base64.b64encode(data)

    # write file out
    out_file = open(filePathOutput, "wb")  # open for [w]riting as [b]inary
    out_file.write(encodedBytes)
    out_file.close()
