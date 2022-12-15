Create directory
```
def createDirIfNotExist(pathDir):
    if not os.path.exists(pathDir):
        os.makedirs(pathDir)
```
Example:
```
createDirIfNotExist("path/to/directory")
```
Save File
```
def saveFile(dataString, filePath):
    # write file out
    out_file = open(filePath, "w")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()
```
Example:
```
saveFile("hola mundo","saved.txt");
```
Save Binary File
```
def saveFileBinary(dataString, filePath):
    # write file out as binary
    out_file = open(filePath, "wb")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()
```
Read Binary File
```
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
```
Example:
```
saveFileBinary(b'hola mundo',"savedBinaryFile.txt");
```
