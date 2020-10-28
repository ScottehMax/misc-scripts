import re

def encode(addr, val, key=0):
    addr = hex(addr)[2:].zfill(4)
    val = hex(val)[2:].zfill(2)
    key = hex(key)[2:].zfill(2)
    bits = ''
    nibs = []
    code = ''
    ln = 9 if key else 6
    if len(addr) != 4 or len(val) != 2 or (key and len(key) != 2):
        return False
    raw = addr + val
    if key:
        raw += key
    if len(re.sub('[0-9A-Fa-f]', '', raw)) != 0:
        return False
    for i in range(len(raw)):
        j = int(raw[i], 16)
        nibs.append(pad(bin(j)[2:], 4))
    bits = nibs[4] + nibs[5] + nibs[1] + nibs[2] + nibs[3] + string_not(nibs[0])
    if ln == 9:
        cbits = string_xor(nibs[6] + nibs[7], '10111010')
        cbits = cbits[2:8] + cbits[0:2]
        shadow = string_xor(cbits[0:4], '1000')
        bits += cbits[0:4] + shadow + cbits[4:8]
    for i in range(ln):
        j = bits[i*4:i*4 + 4]
        j = int(j, 2)
        code += '0123456789ABCDEF'[j]
        if i in {2, 5, 9}:
            code += '-'
    return code

def string_xor(a, b):
    xor = ''
    for i in range(len(a)):
        xor += '0' if a[i] == b[i] else '1'
    return xor

def string_not(a):
    n = ''
    for i in range(4):
        n += '0' if a[i] == '1' else '1'
    return n

def pad(str, pad):
    while len(str) < pad:
        str = '0' + str
    return str