cases = int(raw_input())
money = 0
for i in range(cases):
    intro = raw_input()
    if intro == "report":
        print money
    else:
        money += int(intro.split(" ")[1])
