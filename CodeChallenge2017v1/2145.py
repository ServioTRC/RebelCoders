t = int(raw_input())
for i in range(1, t+1):
    text = raw_input().split(" ")
    lista = []
    for j in range(len(text)):
        lista.append(int(text[j]))
    res = 0
    lista.sort()
    for j in range(1,len(lista)-1):
        res += lista[j]
    print str(i) + " " + str(res)