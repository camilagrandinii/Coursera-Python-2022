def vogal(letra):
	if(testeVogal(letra)):
		return 1
	else:
		return 0

def testeVogal(letra):
  vogais = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
  i=0
  while i<len(vogais):
    if letra==vogais[i]:
      return 1
    i = i+1