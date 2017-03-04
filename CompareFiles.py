try:
    file1 = open('C:\Users\Servio T\Desktop\output.txt','r')
    file2 = open('C:\Users\Servio T\Desktop\output2.txt', 'r')
    datos1 = []
    datos2 = []
    for f in file1:
        datos1.append(f)
    for f in file2:
        datos2.append(f)
    for i in range(len(datos1)):
        if datos1[i] != datos2[i]:
            print datos1[i] + "\t"+datos2[i]
except:
    print "No hay archivos"

