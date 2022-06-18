import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
from manchester_code import encode, decode, decode_bits
from encdec8b10b import EncDec8B10B
from traitlets import dlink
def decode_binary_string(s):
    bitsize= 8
    return ''.join(chr(int(s[i*bitsize:i*bitsize+bitsize],2)) for i in range(len(s)//bitsize))
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

dt_x=[]
dt_y=[]
values = []
count =30000
with open('data.txt', "r") as data:
    lines = data.readlines()
    x = 0
    lasty = 0
    goingUp = True
    for l in lines:
        x = x + 1
        dt_x.append(x)
        y = float(l.strip())
        if goingUp and y < lasty:
            # print("y=", y, " lasty=", lasty)
            goingUp = False
            if lasty > 1.2:
                values.append(1)
            else:
                values.append(0)
        elif not goingUp and y > lasty:
            goingUp = True
        lasty = y
        dt_y.append(y)
        if x > count:
            break
bin_s = ''
bin_s10 = ''
bin_s8 = ''
count = 0
for i in values:
    bin_s = bin_s + str(i)
    bin_s10 = bin_s10 + str(i)
    if count < 8:
        bin_s8 = bin_s8 + str(i)
    count = count + 1
    if count == 10:
        bin_s = bin_s + ' '
        count = 0

print(len(bin_s), " : ", bin_s)
#print(len(bin_s8), " : ", bin_s8)
print(len(bin_s10), " : ", bin_s10)
flag = ''
for token in wrap(bin_s10, 10):
    int_token = int(token, 2)
    hex_token = int(hex(int_token), 16)
    print("s10: "+token +" => "+str(int_token)+" => "+str(hex_token))

    ctrl, decoded = EncDec8B10B.dec_8b10b(hex_token) 
    print(str(hex(decoded)))
    print(str(chr(decoded)))
    flag = flag + str(chr(decoded))
print (flag)

# visualize reduce n to zw 200
#plt.plot(dt_x, dt_y)
#plt.show() #output shown in figure_1

#print(decode_binary_string(bin_s8))
#binary_array = bitstring_to_bytes(bin_s)
#binary_int = int(bin_s8, 2)

#print(decode(values)) #MANCHESTER

# Getting the byte number
#byte_number = binary_int.bit_length() + 7 // 8
  
# Getting an array of bytes
#binary_array = binary_int.to_bytes(byte_number, "big")
#print(binary_array)
# print(decode(binary_array)) #MANCHESTER
# Converting the array into ASCII text
#ascii_text = binary_array.decode()
  
# Getting the ASCII value
#print(ascii_text)
'''
string = "404CTF{"
binary_converted = ' '.join(format(ord(c), 'b') for c in string)
print("The Binary Representation is:", binary_converted)
'''
#b = bin(int(binascii.hexlify(bin_s10.encode()), 16))
#print(b, " => ", binascii.hexlify(bin_s10.encode()), 16)
#s = bin_s7[0:10*8+7]
#sample = "110100001100000011010001000011010101000100011001111011"
'''print(decode_binary_string(s))
#plt.plot(dt_x, dt_y)
#plt.show() #output shown in figure_1
binary_array = bitstring_to_bytes(s)
ascii_text = "Bin string cannot be decoded"
for enc in ['utf-8', 'ascii', 'ansi']:
    try:
        ascii_text = binary_array.decode(encoding=enc)
        break
    except:
        pass
    print(ascii_text)

sampleInt = int(sample, 2)
print("sample : "+sample +" => "+str(sampleInt)+" => "+str(hex(sampleInt)))
'''
