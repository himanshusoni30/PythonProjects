for x in range(0,9):
	str1 = "\U0001f600"
	y = x
	while y >= 0:
		str2 = "\U0001f600"
		y -= 1
	print(str1 + str2*x)

for x in range(0,10):
	print("\U0001f600"*x)
print()
for x in range(9,0,-1):
	print("\U0001f600"*x)

for x in range(10,0,-1):
	str1 = "  "*x
	y = 10
	count=0
	while y >= x:
		y -= 1
		str2 = "\U0001f600"*count
		count+=1		
		# print("y: "+str(y))	
	print(str1+str2)



