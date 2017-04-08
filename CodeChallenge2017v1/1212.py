while True:
    text = raw_input()
    if text == '*':
        break
    notas = text.split("/")
    buenas = 0
    for i in range(len(notas)):
        suma = 0.0
        for j in notas[i]:
            if j == 'W':
                suma += 1
            elif j == 'H':
                suma += 0.5
            elif j == 'Q':
                suma += 0.25
            elif j == 'E':
                suma += 0.125
            elif j == 'S':
                suma += 0.0625
            elif j == 'T':
                suma += 0.03125
            elif j == 'X':
                suma += 0.015625
        if suma == 1.0:
            buenas += 1
    print buenas