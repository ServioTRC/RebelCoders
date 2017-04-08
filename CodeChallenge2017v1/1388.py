t = int(raw_input())
for i in range(t):
    text = raw_input().split(" ")
    num = int(text[0])
    base = num % 10
    expo = int(text[1])
    if expo == 0:
        print 1
    elif expo == 1:
        print num
    elif base == 0:
        print 0
    elif base == 1:
        print 1
    elif base == 2:
        temp = expo % 4
        if temp == 1:
            print 2
        elif temp == 2:
            print 4
        elif temp == 3:
            print 8
        else:
            print 6
    elif base == 3:
        temp = expo % 4
        if temp == 1:
            print 3
        elif temp == 2:
            print 9
        elif temp == 3:
            print 7
        else:
            print 1
    elif base == 4:
        temp = expo % 4
        if temp == 1:
            print 4
        elif temp == 2:
            print 6
        elif temp == 3:
            print 4
        else:
            print 6
    elif base == 5:
        print 5
    elif base == 6:
        print 6
    elif base == 7:
        temp = expo % 4
        if temp == 1:
            print 7
        elif temp == 2:
            print 9
        elif temp == 3:
            print 3
        else:
            print 1
    elif base == 8:
        temp = expo % 4
        if temp == 1:
            print 8
        elif temp == 2:
            print 4
        elif temp == 3:
            print 2
        else:
            print 6
    elif base == 9:
        temp = expo % 4
        if temp == 1:
            print 9
        elif temp == 2:
            print 1
        elif temp == 3:
            print 9
        else:
            print 1