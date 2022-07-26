
num = [0,0,0]
for i in range(3):
  num[i] = int(input())
if num[0]<num[1] and num[1]<num[2]:
	print("crescente")
else:
	print("não está em ordem crescente")