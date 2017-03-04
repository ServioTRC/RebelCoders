cases = int(raw_input())
for i in range(cases):
    text = raw_input().split(" ")
    pricesTXT = raw_input().split(" ")
    prices = []
    for j in range(len(pricesTXT)):
        prices.append(int(pricesTXT[j]))
    changes = []
    valor = prices[0]
    posValor = 0
    for j in range(1, len(prices)):
        if valor > prices[j]:
            changes.append(text[posValor])
            changes.append(text[j])
        else:
            valor = prices[j]
            posValor = j
    changes.sort()

    print changes
