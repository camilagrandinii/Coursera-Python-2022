
fat = 1
num = int(input())
while num>1:
  fat *= num
  num = num - 1
print(fat)

def fat(n):
  fat = 1
  while(n>1):
    fat = fat*n
    n = n-1
  return fat

def testa_fatorial():
  if fatorial(1) == 1:
    print("Funciona para 1")

  else:
    print("Não funciona para 1")

  if fatorial(0) == 1:
    print("Funciona para 0")
  else:
    print(" Não funciona para 1")

