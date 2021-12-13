#!/usr/bin/env python3

flag = b'REDACTED'

def enc(plaintext):
    out = b''
    for c in plaintext:
        h = (int(c & 0xF0) >> 4) - 2
        l = (int(c & 0x0F) + 1) << 4
        print(c, h, l)
        o = int(h) + int(l)

        out += bytes([o])
    return out

# ciphertext = enc(flag)
# print(ciphertext)
# b'UUUUUUUU\x10\xf2BC"\xc5QaT1\x114!T1DD1Ta1d\x81Q4AD4t!\x81a\x11$1dA!\xe5\x10UUUUUUUU'

def dec(ciphertext):
    out = b''
    for i in ciphertext:
        c = 0
        while 1:
            h = (int (c & 0xF0) >> 4) - 2
            l = (int(c & 0x0F) + 1) << 4
            o = int(h) + int(l)
            if(o==i):
                out += bytes([c])
                print(chr(i), end='')
                break
            c += 1
            
    return out

# print(enc(flag))
print(dec(b'UUUUUUUU\x10\xf2BC"\xc5QaT1\x114!T1DD1Ta1d\x81Q4AD4t!\x81a\x11$1dA!\xe5\x10UUUUUUUU'))