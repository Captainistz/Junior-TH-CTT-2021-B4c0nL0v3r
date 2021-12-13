flag = "REDACTED"

def super_encode(flag):
    old = 0
    out = []
    for f in flag:
        new = (ord(f) + old) % 256
        out.append(new)
        old = ord(f)

    return out

def super_decode(arr):
    old = 0
    out = ""
    for a in arr:
        new = (ord(chr(a)) - old) % 256
        out += (chr(new))
        old = ord(chr(new))
        # print(new)
        
    print(out)
secret = super_encode(flag)
dec = super_decode([71, 150, 111, 103, 150, 111, 110, 145, 150, 148, 188, 172, 149, 149, 98, 101, 101, 105, 109, 154, 200, 148, 104, 106, 106, 156, 155, 110, 109, 105, 152, 154, 151, 148, 105, 109, 106, 103, 149, 194, 197, 149, 147, 223, 157, 103, 150, 111, 103, 150])
# print(secret)

# secret = [71, 150, 111, 103, 150, 111, 110, 145, 150, 148, 188, 172, 149, 149, 98, 101, 101, 105, 109, 154, 200, 148, 104, 106, 106, 156, 155, 110, 109, 105, 152, 154, 151, 148, 105, 109, 106, 103, 149, 194, 197, 149, 147, 223, 157, 103, 150, 111, 103, 150]
