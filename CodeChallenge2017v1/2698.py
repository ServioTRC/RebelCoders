t = int(raw_input())
for j in range(t):
    text = raw_input()
    res = 0
    for i in text:
        res += ord(i)-64
    print res