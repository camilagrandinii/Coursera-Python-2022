import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c
raiz = [0]*2

if delta<0:
	print("esta equação não possui raízes reais")
elif delta==0:
	raiz[0] = -b / 2*a
	print("a raiz desta equação é", raiz[0])
else:
	raiz[0] = -b + math.sqrt(delta) / 2*a
	raiz[1] = -b - math.sqrt(delta) / 2*a
	print("as raízes da equação são", raiz[1], "e", raiz[0])

