import glob, os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if fullPath.endswith(".php"):
                allFiles.append(fullPath)
            else:
                continue
    return allFiles


def main():
    paths = getListOfFiles("/Users/divyesh.pal/Documents/")
    string = 'Redis::'
    for path in paths:
        for file in glob.glob(path):
            fileOpened = open(file,'r')
            flag = 0
            index = 0
            for line in fileOpened:
                index += 1
                if string in line:
                    flag = 1
                    break
            if flag == 0:
                continue
            else:
                print(file, string, "found in line index : "+str(index))
            fileOpened.close()

main()
