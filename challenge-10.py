with open('./challenge-10.txt', 'r') as w:
    for i in w.readlines():
        tmp = i[5:-2]
        # print(tmp)
        if tmp[7]=="c" and tmp[15]=="a" and tmp[-1]=="e" and tmp[23]=="f":
            print(tmp)
