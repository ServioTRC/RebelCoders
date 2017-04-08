t = int(raw_input())
res = raw_input()
t = int(raw_input())
for i in range(t):
    calif = 0.0
    text = raw_input()
    for j in range(len(res)):
        if text[j] == '#':
            calif = calif
        elif text[j] == res[j]:
            calif += 1
        elif text[j] != res[j]:
            calif -= 0.25
    print "%0.2f" % calif