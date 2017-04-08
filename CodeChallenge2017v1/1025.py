extra = raw_input()
text = raw_input().split(" ")
lista = []
for i in text:
    lista.append(int(i))
res = 0
lista.sort()
for i in range((len(lista)/2)+1):
    res += (lista[i]/2)+1
print res