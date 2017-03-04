num = int(raw_input())
for i in range(num):
    year = int(raw_input())
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("N")
        else:
            print("S")
    else:
        print("N")
