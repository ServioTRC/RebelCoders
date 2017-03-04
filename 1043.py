t = int(raw_input())
for i in range(t):
    weight = int(raw_input())
    pal = "{0:b}".format(weight)
    for j in range(0,len(pal)):
        if pal[j] == "1":
            print str(j),
    print
print