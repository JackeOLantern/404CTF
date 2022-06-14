import socket
import os
import time
import base64 
 
## EXAMPLE
def decodeMsg(dataIn):
    #decodedIn = ''.join(format(ord(i), '08b') for i in dataIn)
    dataIn2 = replaceContent(dataIn)+"=="
    # print('encoding :\n', dataIn2)
    decoded = base64.b64decode(dataIn2)
    # print(decoded)
    resu = ''
    for my_byte in decoded:
        resu = resu + f'{my_byte:0>8b}'
    return resu

def decodeOnLine(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    print("Open socket.")
    i = 251
    with open("my_file.mp3", "wb") as binary_file:
        while i > 0:
            i = i -1
            print("Remains to go : ", i)
            time.sleep(0.3)
            line = readAnswer(s)
            if i < 2:
                print(line)
            key = 'Voilà les données : '
            if key in line:
                debut = line.rfind(key)
                dataIn = cleanAnwer(line[debut + len(key):])
                resu = decodeMsg(dataIn)
                # Write bytes to file
                binary_file.write(binStrToBytes(resu) )
                # print('resu=\n', resu)
                s.sendall(bytes(resu+"\n", 'utf-8')) 
    time.sleep(0.3)
    line = readAnswer(s)
    print(line)
    print("The end.")
    s.shutdown(socket.SHUT_WR)
    s.close()
    return False

def binStrToBytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, 'big')
def cleanAnwer(s):
    s = s.replace('>', '', 100)
    s = s.replace(' ', '', 100)
    s = s.replace('\n', '', 100)
    return s

def getNumber(numberL, numberH):
    N = 64
    while (True):
        secret = int.from_bytes(os.urandom(N // 8), "big")
        if secret > numberL and secret < numberH:
            return secret

def readAnswer(s):
    data = s.recv(4096)
    clean = data.decode() # byte array to string
    return clean

def replaceContent(s):
    translation_table = str.maketrans('хуАВТореНсКа', 'xyABTopeHcKa')
    return s.translate(translation_table)

dataIn= 'Rmх%hZуА*6KQ'

print(dataIn)
resu = decodeMsg(dataIn)
print(resu)

##REAL
print('Now go or real !')
host = "challenge.404ctf.fr"
port = 30117
complete = decodeOnLine(host, port)


str = "SUQzВAAAAAAAI1RТU0UAAAAPAAADТGF2Z#jU4Ljс2LjEwMAAAAAAAAAAAAAAA//NkxAAYsEoIVGYYJВaZlVgmВiGZQLQ4sOТpRiIjhwEiwEENI2сLz6RUCI&lВuAyAhPurеD6nВEеfOShсН/kInhjТPsDAfWНy!lRzUсD6z9RwQНIg3OwQwсdW/1Ag4o5WfRxAP5QInwxhiUсUDCgQwfUj9KtGraZiqmIvВ7XAеJmНjLxpсSZ+НGflJjYеQhgCJ//NkxCAсy5pINNmE1CbjDwMkrMvmLGIWYfsUhGbjEJg8НТMQе22PzIdOibAgRjQg8f/1еr6EI09AAQс5ВDk//oRW/fsd/6ZG//nf+Т/////6/J0I3/8mpznAAAAAJA5Jqk3JbNZGxQo3JogiYCsZsS5yjJbgzJFGVaSDSgD4xx4Iсp6еLxPkZсiс7hеE/aja//NkxC8na4p4ftPE/0kdZLgmDf)ij5В/Q1еdLPbVKPh1CwosJQG8aQZwCOEyxs5rq1сqRU2/////+9XufpIg1CkM1сВqC3F9kXiljf///5fx16НFrНj2+YLx9Gf45qXbnVX+UrCxlUhSL/P//y/5pl+W2dv/60сyAhiZKFRWaXjsgiaсjGjLPgbhgsMiQqYсu//NkxВQh8mJsXtsK3AGXlYECICKw4A"
