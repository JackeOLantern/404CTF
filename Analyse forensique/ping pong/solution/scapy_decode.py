from scapy.all import  * 
import base64 
import numpy as np

def base64Decode(s):
    # s = byteStr.decode('utf-8')
    # padding
    while (len(s) % 4 != 0):
        s = s + "="
    print(str(len(s)), " : ", s)
    decoded = base64.b64decode(s)
    return decoded
def revxor(ba1):
    """ XOR two byte strings """
    return bytes([_a ^ 0b11111111 for _a in ba1])
network_packets = rdpcap('ping.pcapng')
decoded_commands = [] 
decoded_data ="" 
last = ""
with open("myresult_total.bin", "wb") as binary_file:
    for packet in network_packets:
        if packet.type == 8 or packet[IP].src != '10.1.0.10' and packet.haslayer(ICMP):
            continue
        # decoded_data = str(packet.load)[2:-1] #base64.b64decode(str(packet.an.rdata))
        data_bytes = packet.load
        #if "4567" in data_bytes:
        #    data_bytes = str(data_bytes).replace("4567", "")
        decoded_data +=  packet['ICMP'].load.decode('utf-8', errors="ignore")
        #print('data_bytes', flush=True, end='')
        binary_file.write(data_bytes)
with open("myresult_total2.bin", "wb") as binary_file:
    binary_file.write(base64.b64decode(decoded_data+'=='))
'''        if last != str(data_bytes):
            #    decoded_data = packet.load.decode("hex")
            last = str(data_bytes)
            #b_data = list(data_bytes)
            #print(b_data)
            #binary_file.write(base64Decode(data_bytes))
            decoded_commands.append(data_bytes.decode('ascii'))
total = ''
for command in decoded_commands: 
    if len(command)>1: 
        total = total  + command.rstrip()
        #print(command.rstrip()) 
totalBytes = base64Decode(total)
with open("myresult_total.jpg", "wb") as binary_file:
    binary_file.write(totalBytes)
 
with open("myresult_total3.txt", "wb") as binary_file:
    binary_file.write(revxor(totalBytes))

# also try block by bloc decode
#with open("myresult_parts.txt", "wb") as binary_file:
#    for command in decoded_commands: 
#        part = base64Decode(command)
#        binary_file.write(part)


#full_data = ''.join(decoded_commands)
#decoded = base64.b64decode(full_data)
#print(decoded)
'''
def little(string):
 t= bytearray.fromhex(string)
 t.reverse()
 return ''.join(format(x,'02x') for x in t).upper()

resu = '5054584146 34 53 31 33 32 4f 4d 4d 53 45 39 4e 50 30 54 4a 35 56 49 33'

st = bytes.fromhex(resu).decode('utf-8')
print (st)

resu = little(resu)
st = bytes.fromhex(resu).decode('utf-8')
print (st)
print (resu)

resu = little(resu)
st = bytes.fromhex(resu).decode('utf-8')
print (st)
print (resu)

