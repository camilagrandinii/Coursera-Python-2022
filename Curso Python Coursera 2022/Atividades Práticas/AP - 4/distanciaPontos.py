import math
nums = [0]*4
for i in range(4):
	nums[i] = int(input())
distancia = math.sqrt(((nums[0]-nums[2])**2) + ((nums[1]-nums[3])**2))
if distancia>=10:
	print("longe")
else:
	print("perto")