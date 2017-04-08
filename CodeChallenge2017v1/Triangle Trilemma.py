import math
cases = int(raw_input())
for i in range(1,cases+1):
    print "Case #"+str(i)+":",
    text = raw_input().split(" ")
    points = []
    for j in range(len(text)):
        points.append(int(text[j]))
    a = math.sqrt((points[0]-points[2])**2+(points[1]-points[3])**2)
    b = math.sqrt((points[2]-points[4])**2+(points[3]-points[5])**2)
    c = math.sqrt((points[4]-points[0])**2+(points[5]-points[1])**2)
    s = 0.5*(a+b+c)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    if area == 0.0:
        print "not a triangle"
    else:
        anguloA = int(math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c))))
        anguloB = int(math.degrees(math.acos((c**2-b**2-a**2)/(-2*b*a))))
        anguloC = int(math.degrees(math.acos((b**2-a**2-c**2)/(-2*a*c))))
        if anguloA == 89:
            anguloA+= 1
        if anguloB == 89:
            anguloB+= 1
        if anguloC == 89:
            anguloC+= 1
        if a != c and a != b and b != c:
            ##Es escaleno
            if anguloA > 90.0 or anguloB > 90.0 or anguloC > 90.0:
                print "scalene obtuse triangle"
            elif anguloA < 90.0 and anguloB < 90.0 and anguloC < 90.0:
                print "scalene acute triangle"
            else:
                print "scalene right triangle"
        else:
            ##Es isoceles
            if anguloA > 90 or anguloB > 90 or anguloC > 90:
                print "isosceles obtuse triangle"
            elif anguloA < 90 and anguloB < 90 and anguloC < 90:
                print "isosceles acute triangle"
            else:
                print "isosceles right triangle"