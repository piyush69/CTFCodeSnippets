import socket
import sys
import string


server = 'abc.ab.io'
port = 6969
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '[+] Connecting to server'
s.connect((server, port))

while 1:
    text=s.recv(50)
    print text
    if 'Discover' in text:
        s.send(str(Discover[d])+"\n")
        d += 1
    elif 'American' in text:
        s.send(str(American[a])+"\n")
        a += 1
    elif 'Visa' in text:
        s.send(str(Visa[v])+"\n")
        v += 1
    elif 'MasterCard' in text:
        s.send(str(MasterCard[m])+"\n")
        m += 1
    elif 'starts' in text:
        continue
    elif 'ends' in text:
        l = list(text.split(" "))
        ini = l[-1]
        ini = int(ini[:-2])
        ans = endd[ini][0]
        endd[ini].pop(0)
        #print (ini,str(endi[int(ini)]))
        s.send(str(ans)+"\n")
    else:
        quit()
