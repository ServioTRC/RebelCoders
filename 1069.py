def recursivo(total, costo, suma):
    num = total/costo
    #suma += num
    if (total / costo) == 0:
        return suma
    else:
        return recursivo(num,costo,suma+num)

def botellas(total, costo):
    res = 0
    while total / costo != 0:
        num = total / costo
        res += num
        total = num
    return res


t = int(raw_input())
for i in range(t):
    text = raw_input().split(" ")
    res = 0
    total = int(text[0])
    total += int(text[1])
    costo = int(text[2])
    res = botellas(total, costo)
    print res