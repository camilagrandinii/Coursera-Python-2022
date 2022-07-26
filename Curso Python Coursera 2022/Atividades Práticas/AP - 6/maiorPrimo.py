def maior_primo(n):
  if n>=2:
    while n>2:
      if ePrimo(n):
        return n
      else:
        n = n - 1

def ePrimo(n):
	ePrimo = 1
	for i in range(n):
		if i and n%i==0 and i!=1:
			ePrimo=0
	return ePrimo

maior_primo(100)