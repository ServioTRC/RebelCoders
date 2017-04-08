t = int(raw_input())
for i in range(t):
    entrada = raw_input().split(" ")
    nums = int(entrada[1])**2 - 4 * int(entrada[0])*int(entrada[2])
    if nums >= 0:
        print "SI"
    else:
        print "NO"
