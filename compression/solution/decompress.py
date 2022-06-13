import os

def decompress(filename):
    command = '"C:\\Program Files\\WinRAR\\winrar.exe" x '+filename #command to be executed
    res = os.system(command)

def getFileName(i):
    for x in os.listdir():
        if str(i) in x:
            return x
    return None

for i in range (0, 2500):
    fileName = getFileName(2500 - i)
    print(fileName)
    decompress(fileName)
    if i < 2498:
        os.remove(fileName)
