t = int(raw_input())
for i in range(t):
    res = 0
    text = raw_input().split(" ")
    px1 = int(text[0])
    px2 = int(text[2])
    py1 = int(text[1])
    py2 = int(text[3])
    #X's
    if px1 > px2:
        res += px1 - px2
    else:
        res += px2 - px1
    #Y's
    if py1 > py2:
        res += py1 - py2
    else:
        res += py2 - py1
    print res