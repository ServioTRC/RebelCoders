t = int(raw_input())
for i in range(t):
    weight = int(raw_input())
    pal = "{0:b}".format(weight)
    extra = []
    for j in pal:
        extra.append(j)
    extra.reverse()
    for j in range(len(extra)):
        if extra[j] == "1":
            print str(j),
    print