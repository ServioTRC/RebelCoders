print "n e"
print "- -----------"
res = 0.0
for i in range(0, 10):
    acu = 1.0
    for j in range(1,i+1):
        acu *= j
    res += (1/acu)
    print str(i)+" "+str(res)
