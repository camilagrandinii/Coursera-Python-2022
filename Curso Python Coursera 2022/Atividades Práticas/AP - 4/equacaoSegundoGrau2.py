import math
def delta(a, b, c):
	return (b**2) - (4*a*c)

def main():
	a = float(input("Digite o valor de a: "))
	b = float(input("Digite o valor de b: "))
	c = float(input("Digite o valor de c: "))
	imprime_raizes(a,b,c)

def imprime_raizes(a,b,c):
  raiz=[0]*2
  d = delta(a,b,c)
  if d<0:
    print("Esta equação não possui raízes reais")
  elif d==0:
    raiz[0] = -b / 2*a
    print("A raiz desta equação é", raiz[0])
  else:
    raiz[0] = (-b + math.sqrt(d)) / (2*a)
    raiz[1] = (-b - math.sqrt(d)) / (2*a)
    print("As raízes da equação são", raiz[1], "e", raiz[0])
