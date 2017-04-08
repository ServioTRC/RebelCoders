def gdc(num1, num2):
    while True:
        if num1 % num2 == 0:
            return num2
        res = num1 % num2
        num1 = num2
        num2 = res


num1 = int(raw_input("Primer Numero:"))
num2 = int(raw_input("Segundo Numero:"))
if num1 >= num2:
    print gdc(num1,num2)
else:
    print gdc(num2, num1)