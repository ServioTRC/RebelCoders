t = int(raw_input())
#ASCII VALUES MAYUS 65-90
#MINUS 97 - 122
for i in range(t):
    text = raw_input()
    mayus = 0
    minus = 0
    for j in text:
        if ord(j) >= 97:
            minus += 1
        else:
            mayus += 1
    if minus == mayus:
        print "SI"
    else:
        print "NO"