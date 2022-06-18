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


network_packets = rdpcap('ransomware1.pcapng')
data = [] 
counter = 500000
for packet in network_packets:
    #if packet.type == 8 or packet[IP].src != '172.17.0.2':
    if counter <= 0 or not IP in packet or packet[IP].src != '172.17.0.1':
        continue
    counter = counter - 1
   #hex = hexdump(packet, False)

    hex = bytes_encode(packet)[47:48]
    data.append(hex)
    print("packet : ", packet[IP].src, " --> ",  packet[IP].dst, " : ", hex)

with open("myresult.txt", "wb") as binary_file:
    for b in data:
        binary_file.write(b)
'''
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
'''
# also try block by bloc decode
#with open("myresult_parts.txt", "wb") as binary_file:
#    for command in decoded_commands: 
#        part = base64Decode(command)
#        binary_file.write(part)


#full_data = ''.join(decoded_commands)
#decoded = base64.b64decode(full_data)
#print(decoded)



