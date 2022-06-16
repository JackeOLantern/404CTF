import zlib
import struct
import matplotlib.pyplot as plt
import numpy as np

f = open('stage3.png', 'rb')

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
'''
IDAT_dataLast = b''.join(chunk_data for chunk_type, chunk_data in lastChunkData if chunk_type == b'IDAT')
IDAT_dataLast = zlib.decompress(IDAT_dataLast)

with open("last_data.txt", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(IDAT_dataLast)
'''

with open("last_data2.txt", "wb") as binary_file:
    # Write bytes to file
    binary_file.write(IDAT_data)

def PaethPredictor(a, b, c):
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        Pr = a
    elif pb <= pc:
        Pr = b
    else:
        Pr = c
    return Pr

Recon = []
bytesPerPixel = 4
stride = width * bytesPerPixel

def Recon_a(r, c):
    return Recon[r * stride + c - bytesPerPixel] if c >= bytesPerPixel else 0

def Recon_b(r, c):
    return Recon[(r-1) * stride + c] if r > 0 else 0

def Recon_c(r, c):
    return Recon[(r-1) * stride + c - bytesPerPixel] if r > 0 and c >= bytesPerPixel else 0

i = 0
for r in range(height): # for each scanline
    filter_type = IDAT_data[i] # first byte of scanline is filter type
    i += 1
    for c in range(stride): # for each byte in scanline
        Filt_x = IDAT_data[i]
        i += 1
        if filter_type == 0: # None
            Recon_x = Filt_x
        elif filter_type == 1: # Sub
            Recon_x = Filt_x + Recon_a(r, c)
        elif filter_type == 2: # Up
            Recon_x = Filt_x + Recon_b(r, c)
        elif filter_type == 3: # Average
            Recon_x = Filt_x + (Recon_a(r, c) + Recon_b(r, c)) // 2
        elif filter_type == 4: # Paeth
            Recon_x = Filt_x + PaethPredictor(Recon_a(r, c), Recon_b(r, c), Recon_c(r, c))
        else:
            raise Exception('unknown filter type: ' + str(filter_type))
        Recon.append(Recon_x & 0xff) # truncation to byte


plt.imshow(np.array(Recon).reshape((height, width, 4)))
plt.show()