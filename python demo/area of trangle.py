a = float(input("length of side 1: "))
b = float(input("length of side 2: "))
c = float(input("length of side 3: "))

s = (a + b + c) / 2

area = (s*(s-1)*(s-b)*(s-c))**0.5
print('Area is {0:0.2f}'.format(area))