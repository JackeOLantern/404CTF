import socket
import io
import time
from base64 import b64decode
from PIL import Image
def decodeDoors(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    print("Open socket.")
    i = 129
    while i > 0:
        print("Remains to go : ", i)
        line = readAnswer(s)
        print(line)
        key = 'Vite vite vite !!!'
        key2 = '\n>>'
        total = ''
        if key in line:
            begin = line.rfind(key)
            end = line.rfind(key2)
            dataIn = cleanAnwer(line[begin + len(key):end])
            print(dataIn)
            decoded = b64decode(dataIn)
            # filename = 'image_'+str(i)+'.png'
            #with open(filename, 'wb') as output_file:
            #    output_file.write(decoded)
            img1 = Image.open(io.BytesIO(decoded))
            img1.save('origin_a.png')
            width1, height1 = img1.size 
            # print("img1 %d, %d"%(width1, height1))
            rgb_im = img1.convert('RGB')
           
            r, g, b = rgb_im.getpixel((1, 1))
            buf = ''
            d = decode128Dict()
            for x in range(0, width1):
                r, g, b = rgb_im.getpixel((x, 1))
                #if x % 3 != 0:
                #    continue
                if r < 128:
                    buf = buf = buf + '1'
                else:
                    buf = buf = buf + '0'
                if len(buf) == 11:
                    c = d[buf]
                    # print(buf+" => "+c)
                    total = total + c
                    buf = ''
            print("total : ", total)
        s.sendall(bytes(str(total)+"\n", 'utf-8')) 
        time.sleep(0.2)
        i = i - 1
    print("The end.")
    s.shutdown(socket.SHUT_WR)
    s.close()
    return False

def cleanAnwer(s):
    s = s.replace(' ', '', 10)
    s = s.replace('\n', '', 10)
    return s

def readAnswer(s):
    data = s.recv(4096)
    clean = data.decode() # byte array to string
    return clean

def decode128Dict():
    d = dict()
    d['11011001100']=' '
    d['11001101100']='!'
    d['11001100110']='"'
    d['10010011000']='#'
    d['10010001100']='$'
    d['10001001100']='%'
    d['10011001000']='&'
    d['10011000100']='\''
    d['10001100100']='('
    d['11001001000']=')'
    d['11001000100']='*'
    d['11000100100']='+'
    d['10110011100']=','
    d['10011011100']='-'
    d['10011001110']='.'
    d['10111001100']='/'
    d['10011101100']='0'
    d['10011100110']='1'
    d['11001110010']='2'
    d['11001011100']='3'
    d['11001001110']='4'
    d['11011100100']='5'
    d['11001110100']='6'
    d['11101101110']='7'
    d['11101001100']='8'
    d['11100101100']='9'
    d['11100100110']=':'
    d['11101100100']=';'
    d['11100110100']='<'
    d['11100110010']='='
    d['11011011000']='>'
    d['11011000110']='?'
    d['11000110110']='@'
    d['10100011000']='A'
    d['10001011000']='B'
    d['10001000110']='C'
    d['10110001000']='D'
    d['10001101000']='E'
    d['10001100010']='F'
    d['11010001000']='G'
    d['11000101000']='H'
    d['11000100010']='I'
    d['10110111000']='J'
    d['10110001110']='K'
    d['10001101110']='L'
    d['10111011000']='M'
    d['10111000110']='N'
    d['10001110110']='O'
    d['11101110110']='P'
    d['11010001110']='Q'
    d['11000101110']='R'
    d['11011101000']='S'
    d['11011100010']='T'
    d['11011101110']='U'
    d['11101011000']='V'
    d['11101000110']='W'
    d['11100010110']='X'
    d['11101101000']='Y'
    d['11101100010']='Z'
    d['11100011010']='['
    d['11101111010']='\\'
    d['11001000010']=']'
    d['11110001010']='^'
    d['10100110000']='_'
    d['10100001100']='`'
    d['10010110000']='a'
    d['10010000110']='b'
    d['10000101100']='c'
    d['10000100110']='d'
    d['10110010000']='e'
    d['10110000100']='f'
    d['10011010000']='g'
    d['10011000010']='h'
    d['10000110100']='i'
    d['10000110010']='j'
    d['11000010010']='k'
    d['11001010000']='l'
    d['11110111010']='m'
    d['11000010100']='n'
    d['10001111010']='o'
    d['10100111100']='p'
    d['10010111100']='q'
    d['10010011110']='r'
    d['10111100100']='s'
    d['10011110100']='t'
    d['10011110010']='u'
    d['11110100100']='v'
    d['11110010100']='w'
    d['11110010010']='x'
    d['11011011110']='y'
    d['11011110110']='z'
    d['11110110110']='{'
    d['10101111000']='|'
    d['10100011110']='}'
    d['10001011110']='~'
    d['10111101000']='Ã'
    d['10111100010']='Ä'
    d['11110101000']='Å'
    d['11110100010']='Æ'
    d['10111011110']='Ç'
    d['10111101110']='È'
    d['11101011110']='É'
    d['11110101110']='Ê'
    d['11010000100']='Ë'
    d['11010010000']='Ì'
    d['11010011100']='Í'
    d['11000111010']='—'
    d['11010111000']='—'
    d['1,10001E+12']='Î'
    return d



host = "challenge.404ctf.fr"
port = 30566
complete = decodeDoors(host, port)
