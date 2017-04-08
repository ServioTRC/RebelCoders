t = int(raw_input())
for i in range(t):
    text = raw_input()
    lista = []
    for j in text:
        if j not in lista:
            lista.append(j)
    print len(lista)