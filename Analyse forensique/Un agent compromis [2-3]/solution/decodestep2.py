
import binascii
fileHex = ['666c61672e747874', '68616c6c6562617264652e706e67', '73757065722d7365637265742e706466', '657866696c74726174696f6e2e7079']
resu = []

for f in fileHex:
    # binascii.hexlify(filename.encode()).decode()
    fileHex2 = binascii.unhexlify(f.encode()).decode()
    resu.append(fileHex2)

print(sorted(resu))
flag = ''#
for f in sorted(resu):
    if (len(flag) > 0):
        flag = flag + ','
    flag = flag + f
flag = '404CTF{' + flag + '}'
print(flag)