import os


def getPath():
    currentPath = os.getcwd()

    # generate the aperance of the terminal of the user to make inputs
    print(f"\x1b[91m{os.path.basename(currentPath)}\x1b[0m:", currentPath)


def generateFolderReport():
    # Creating new folders for the final report
    reportsFolder = "reportsCampana"
    
    if not os.path.exists(reportsFolder):
        os.makedirs(reportsFolder)
        print(f"Folder " + reportsFolder + " created successfully!")
    else:
        print(f"Folder " + reportsFolder + " already exists")

