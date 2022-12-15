def saveFile(dataString, filePath):
    # write file out
    out_file = open(filePath, "w")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()


def saveFileBinary(dataString, filePath):
    # write file out as binary
    out_file = open(filePath, "wb")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()


def readFileBinary(filePathInput):
    if os.path.isfile(filePathInput):
        print('File exists: ' + str(os.path.isfile(filePathInput)))
    else:
        print('File not found!')
        sys.exit()

    # read file
    in_file = open(filePathInput, "rb")  # opening for [r]eading as [b]inary
    data = in_file.read()  # data have file in memory
    in_file.close()
    return data;
