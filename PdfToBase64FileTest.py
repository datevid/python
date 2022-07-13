from PdfToBase64File import PdfToBase64File

if __name__ == '__main__':
    filePathInput = "/home/doctor/CEA/pdfs/obs/examplepdf1.pdf";
    filePathOutput = filePathInput + ".out.txt";
    PdfToBase64File(filePathInput, filePathOutput)
