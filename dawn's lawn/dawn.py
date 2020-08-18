def grow(list, len):
	for x in  range (len):
		if list[x] == '|':
			list[x] = '*'
		elif list[x] == '/':
			list[x] = '|'
		elif list[x] == '-':
			list[x] = '/'
		elif list[x] == '\\':
			list[x] = '-'
		elif list[x] == '_':
			list[x] = '\\'

def cut(list, x):

	if list[x] == '*':
		list[x] = '/'
	elif list[x] == '|':
		list[x] = '-'
	elif list[x] == '/':
		list[x] = '\\'
	elif list[x] == '-':
		list[x] = '_'
	elif list[x] == '\\':
		list[x] = '.'
	elif list[x] == '_':
		list[x] = '.'	


with open("dawn2.txt") as textFile:
	lines  = [line.split() for line in textFile]
	
	size = 20
	counter = 0
	list = []
		

	for x in range(size):
		if x % 2 == 0:
			for n in range(size):
				if (counter % size == 0) and (counter != 0):
					grow(list, len(list))
				list.append(lines[n][0][x])
				cut(list, len(list) - 1)
				counter += 1
		elif x % 2 == 1:
			for n in reversed(range(size)):
				if (counter % size == 0) and (counter != 0):
					grow(list, len(list))
				list.append(lines[n][0][x])
				cut(list, len(list) - 1)
				counter += 1


	flowers = 0
	for x in  range (len(list)):
		if list[x] == '*':
			flowers += 1

	print(flowers)

	

	

	