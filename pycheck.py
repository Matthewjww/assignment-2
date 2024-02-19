def printFile():
    fileName: str = input("Please enter the file to check \n")
    # print(fileName)

    file = open(fileName, "r")
    for line in file:

    file.close()
