text = input()
count = 0
'''
for char in text:
	if char.upper() == 'G' or char.upper() == 'C' or char.upper() == 'T' or char.upper() == 'A':
		if char.upper() == 'G':
			print('C',end='')
		elif char.upper() == 'C':
			print('G',end='')
		elif char.upper() == 'T':
			print('A',end='')
		elif char.upper() == 'A':
			print('U',end='')
	else:
		print('Invalid Input')
		break
'''
restrict = ['G','C','T','A']
for char in text:
	if char not in restrict:
		print('Invalid Input')
		break
	else:
		if char.upper() == 'G':
			print('C',end='')
		elif char.upper() == 'C':
			print('G',end='')
		elif char.upper() == 'T':
			print('A',end='')
		elif char.upper() == 'A':
			print('U',end='')

'''
Actual Solution of Hacker Earth:

b=input()
a="GCTA";c="CGAU"
try:print(''.join([c[a.index(i)]for i in b]))
except:print("Invalid Input")
'''


		

