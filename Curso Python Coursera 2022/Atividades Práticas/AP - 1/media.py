media=0
for num in range(1,5):
	nota = int(input())
	media += nota
media = round(media/4, 2)
print("A média aritmética é", media)