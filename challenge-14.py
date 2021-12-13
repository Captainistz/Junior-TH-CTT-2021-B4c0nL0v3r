import math

KEY = 'REDACTED'
FLAG = 'REDACTED'

# n = int.from_bytes(os.urandom(1), 'little')
# print(f'{n=}')

def encode_key(n, KEY):
    key = []

    for k in KEY[0::2] + KEY[1::2]:
        o = ord(k) ^ n
        key.append(bytes([o]))

    return b''.join(key)
    


en_key = b'\xd7\xfb\xe1\xe7\xed\xf6\xf2\xee\xe2\xff\xfe\xf8\xf2\xfe\xed\xe1\xe5\xfa\xf4\xb6'

def encode_flag():
    key = (KEY * int(len(FLAG)/len(KEY) + 1))[:len(FLAG)]

    out = []
    for f, k in zip(FLAG, key):
        s = ord(f) ^ ord(k)
        out.append(bytes([s]))

    return b''.join(out)

en_flag = encode_flag()
print(en_flag)

en_flag = b'2\x06\x1f\n\x05E\x11\x1b\x1fZ\x13\x13\x01^Y\x1b\x1c\x0c\x04D4\x1aL\x0e\x04\x00P\x0b\x16\x0f\x04ZE\x1a\x1c\x1f\x10C\x01R`\x1d\x04\nV\x16\x15\n\x08\x1f\x15ZE<:>4\x18P@!PZ]AUHY\x19JQ\x12WF\x1b\x08\x14U\t\x12$^\x0e^\x13PH\x0f\x19O\x1cV\x0c\x01Y\x0b\x1a\x11HX/\x1c'

def super_decode():
    for i in range(1, 156):
        print(i)
        rk = ""
        for ek in en_key:
            rk += chr(ek^i)
        bh = rk[math.ceil(len(rk)/2):]
        fh = rk[:math.ceil(len(rk)/2)]
        tk = ""
        for j in range(len(bh)):
            tk += fh[j] + bh[j]
        if len(fh) > len(bh):
            tk += fh[-1]

        real_k = (tk * int(len(en_flag)/len(tk) + 1))[:len(en_flag)]
        for f, ky in zip(en_flag, real_k):
            print(chr(ord(ky)^f), end='')
        print('\n')
        print(real_k)

super_decode()
        
