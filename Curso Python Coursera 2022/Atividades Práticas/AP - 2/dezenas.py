num = input()
lenghtString = len(num)
if lenghtString>1:
	print("O dígito das dezenas é", num[lenghtString-2])
elif lenghtString==1:
	print("O dígito das dezenas é 0")