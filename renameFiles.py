import os, sys

if(len(sys.argv) != 3):
    print("Invalid Usage ! syntax: python renameFiles.py <old pattern in string> <new pattern in string>")
    sys.exit()

#Recursively call the function to rename all the files
def renameFile(path, folder):
    os.chdir(os.path.join(path, folder))
    temp = os.getcwd()
    listOfFiles = os.listdir(temp)
    for f in listOfFiles:
        if os.path.isdir(os.path.join(temp,f)) and "." not in f:
            renameFile(temp,f)
        elif os.path.isfile(os.path.join(temp,f)):
            os.chdir(temp)
            os.rename(f,f.replace(str(sys.argv[1]),str(sys.argv[2])))

home = os.getcwd()
currentFolder = (os.getcwd()).split("/")[-1]
currentFolderPath = home[:(-1*len(currentFolder))]

renameFile(currentFolderPath, currentFolder)
