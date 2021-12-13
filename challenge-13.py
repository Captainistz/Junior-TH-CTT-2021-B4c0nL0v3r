import os

flag = "REDACTED"

def super_encode(flag):
    old = sum(os.urandom(8))
    out = []
    for f in flag:
        new = (ord(f) - old) % 256
        out.append(new)
        old = ord(f)

    return out
    
def super_decode(arr):
    for old in range(1, 2000):
        # old = sum(os.urandom(8))
        print(old)
        out = ""
        for a in arr:
            new = (ord(chr(a)) + old) % 256
            out += (chr(new))
            old = ord(chr(new))
        if "NCSA" in out:
            print(out)


print(super_decode([189, 20, 253, 187, 70, 6, 245, 6, 185, 73, 10, 173, 46, 245, 16, 238, 58, 184, 4, 252, 49, 207, 0, 5, 42, 213, 42, 5, 253, 0, 209, 1, 251, 52, 208, 4, 254, 3, 43, 212, 41, 211, 253, 3, 45, 0, 214, 255, 1, 70, 177, 242, 55, 14, 7, 0, 180, 36, 43, 255, 247]))
# secret = [189, 20, 253, 187, 70, 6, 245, 6, 185, 73, 10, 173, 46, 245, 16, 238, 58, 184, 4, 252, 49, 207, 0, 5, 42, 213, 42, 5, 253, 0, 209, 1, 251, 52, 208, 4, 254, 3, 43, 212, 41, 211, 253, 3, 45, 0, 214, 255, 1, 70, 177, 242, 55, 14, 7, 0, 180, 36, 43, 255, 247]

