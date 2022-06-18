import zlib
import struct
import matplotlib.pyplot as plt
import numpy as np

f = open('step3_fin.png', 'rb')

PngSignature = b'\x89PNG\r\n\x1a\n'
if f.read(len(PngSignature)) != PngSignature:
    raise Exception('Invalid PNG Signature')

def read_chunk(f):
    # Returns (chunk_type, chunk_data)
    chunk_length, chunk_type = struct.unpack('>I4s', f.read(8))
    chunk_data = f.read(chunk_length)
    chunk_expected_crc, = struct.unpack('>I', f.read(4))
    chunk_actual_crc = zlib.crc32(chunk_data, zlib.crc32(struct.pack('>4s', chunk_type)))
    if chunk_expected_crc != chunk_actual_crc:
        raise Exception('chunk checksum failed')
    return chunk_type, chunk_data

chunks = []
# lastChunkData = []
while True:
    chunk_type, chunk_data = read_chunk(f)
    chunks.append((chunk_type, chunk_data))
    print("Chunk type "+str(chunk_type))
    if chunk_type == b'IEND':
        break
    #elif chunk_type == b'IDAT':
    #    lastChunkData.append((chunk_type, chunk_data))

_, IHDR_data = chunks[0] # IHDR is always first chunk
width, height, bitd, colort, compm, filterm, interlacem = struct.unpack('>IIBBBBB', IHDR_data)
if compm != 0:
    raise Exception('invalid compression method')
if filterm != 0:
    raise Exception('invalid filter method')
if colort != 6:
    raise Exception('we only support truecolor with alpha')
if bitd != 8:
    raise Exception('we only support a bit depth of 8')
if interlacem != 0:
    raise Exception('we only support no interlacing')

IDAT_data = b''.join(chunk_data for chunk_type, chunk_data in chunks if chunk_type == b'IDAT')
IDAT_data = zlib.decompress(IDAT_data)
# Write bytes to file
with open("step4_data.dat", "wb") as binary_file:
    binary_file.write(IDAT_data)
# search

with open("step4_filter.dat", "wb") as f2:
    position = 0
    with open("step4_data.dat", "rb") as f:
        while True:
            b = f.read(1)
            if not b:
                break # end of file
            # we keep only filtering bytes : the first byte of eachline
            # that is every 800 x 4 + 1 bytes (800 pixels per line , 4 color per pixel RVBA + 1 = filtering byte)
            if position % (800 * 4 + 1) == 0:
                print(position)
                f2.write(b)
            position = position + 1

data = []
dataStr = ''
with open("step4_filter.dat", "rb") as f:
    while True:
        b = f.read(1)
        # we attempt to decode base4 and ignore char when byte > 4
        if not b or ord(b) >= 4:
            break # end of file
        data.append(ord(b))
        dataStr = dataStr + str(ord(b))
print(data)
print(dataStr)
valDecoded = int(dataStr, 4)
print(valDecoded)
# print(f"This is the number in hexadecimal: {valDecoded :x}")
valHex = hex(valDecoded)
print(f"This is the number in hexadecimal: {valHex}")
# convert hex string to ASCII string
bytes_array = bytes.fromhex(valHex[2:])
ascii_str = bytes_array.decode()

# printing ASCII string
print('ASCII String:', ascii_str)