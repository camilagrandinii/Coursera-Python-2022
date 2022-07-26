num = input()
tamString = len(num)
soma=0
num = int(num)
for i in range(tamString):
	soma += num%10
	num = num // 10
print(soma)
