
def buildLayout(characterMap):
	mapped = set()
	def mapLine(l):
		if 'output="' not in l: return l
		first, third = l.split('output="')
		second = 'output="'
		third, fourth = third.split('"')
		if third in characterMap:
			mapped.add(third)
			return ''.join([first, second, characterMap[third], fourth])
		else:
			return l
	open('custom.keylayout', 'w').write(''.join(map(mapLine, open('US.keylayout')))
	return mapped
