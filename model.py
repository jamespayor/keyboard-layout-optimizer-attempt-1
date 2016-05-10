from collections import defaultdict

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap

class TypingModel(object):

	defaultLayout = r'''

 * * * *   * * * *
00 1 2 33 44 5 6 7777

~! @ # $% ^& * ( )_+ 
`1 2 3 45 67 8 9 0-= 

 Q W E RT YU I O P{}|
 q w e rt yu i o p[]\

 A S D FG HJ K L :"
 a s d fg hj k l ;'   <=

 Z X C VB NM < > ?
 z x c vb nm , . /

	'''

	# With index finger in home position being 1.0, how hard is it to press each key?
	# Costs aren't symmetric, because in my case it's different for each hand, and
	# keyboards tend to have slanted columns (e.g. N is easier to press than B).
	keyCost = [list(map(float, l.strip().split())) for l in [l for l in '''

|---Pinky|Ring|-Mid-|Index--|  |--Index|-Mid-|Ring|Pinky------------|

12.0 10.0  3.0  3.0  4.0  4.0  4.5  3.0  3.0  3.0 12.0 16.0 20.0
      8.0  2.2  1.5  1.6  2.5  3.0  1.6  1.5  2.2  8.0  8.0 12.0 16.0
      4.0  2.0  1.5  1.0  1.4  1.4  1.0  1.5  2.0  4.0  6.0
      5.0  4.0  3.0  1.2  2.5  2.0  1.2  3.0  4.0  6.0

	'''.splitlines() if l.strip()][1:]]

	defaultLayoutLines = tuple(line for line in defaultLayout.splitlines() if line.strip())

	fingerAssignment = tuple(int(character) if character != ' ' else None for character in defaultLayoutLines[1])
	verticalHome = (iter(index / 2 for index, line in enumerate(defaultLayoutLines[2:]) if line[-2:] == '<=').next(),) * 8
	horizontalHome = tuple(index for index, character in enumerate(defaultLayoutLines[0]) if character == '*')

	def stringToLayout(s):
		lines = [line for line in map(str.strip, s.splitlines()) if line]
		return tuple(
			tuple(upperChar + lowerChar for upperChar, lowerChar in zip(upperLine, lowerLine) if upperChar.strip() or lowerChar.strip())
			for upperLine, lowerLine in zip(lines[::2], lines[1::2])
		)

	defaultLayoutRows = stringToLayout('\n'.join(line.strip() for line in defaultLayoutLines[2:]))
	layoutColumnMap = tuple(tuple(line.index(character) for character in line.strip() if character != ' ') for line in defaultLayoutLines[2::2])


	QWERTY = stringToLayout(r'''
		~!@#$%^&*()_+
		`1234567890-=

		QWERTYUIOP{}|
		qwertyuiop[]\

		ASDFGHJKL:"
		asdfghjkl;'

		ZXCVBNM<>?
		zxcvbnm,./
	''')

	DVORAK = stringToLayout(r'''
		~!@#$%^&*(){}
		`1234567890[]
		
		"<>PYFGCRL?+|
		',.pyfgcrl/=\
		
		AOEUIDHTNS_
		aoeuidhtns-

		:QJKXBMWVZ
		;qjkxbmwvz
	''')

	PDVORAK = stringToLayout(r'''
		~%7531902468`
		$&[{}(=*)+]!#
		
		:<>PYFGCRL?^|
		;,.pyfgcrl/@\
		
		AOEUIDHTNS_
		aoeuidhtns-

		"QJKXBMWVZ
		'qjkxbmwvz
	''')

	COLEMAK = stringToLayout(r'''
		~!@#$%^&*()_+
		`1234567890-=

		QWFPGJLUY:[]\
		qwfpgjluy;{}|

		ARSTDHNEIO"
		arstdhneio'

		ZXCVBKM<>?
		zxcvbkm,./
	''')

	WORKMAN = stringToLayout(r'''
		~!@#$%^&*()_+
		`1234567890-=

		QDRWBJFUP:{}|
		qdrwbjfup;[]\

		ASHTGYNEOI"
		ashtgyneoi'

		ZXMCVKL<>?
		zxmcvkl,./
	''')

	ALPHA = stringToLayout(r'''
		~!@#$%^&*(){}
		`1234567890[]

		ZYKDL"|UCWXQJ
		zykdl'\ucwxqj

		>MITFSENRV?
		.mitfsenrv/

		:_PA<HOGB+
		;-pa,hogb=
	''')

	BETA = stringToLayout(r'''
		~!@#$%^&*(){}
		`1234567890[]

		Z>:_C|<PDW"+Q
		z.;-c\,pdw'=q

		?FHTIRESMBJ
		/fhtiresmbj

		VYLAGKONUX
		vylagkonux
	''')

	GAMMA = stringToLayout(r'''
		~!@#$%^&*(){}
		`1234567890[]

		?_WHA"BCMGYQZ
		/-wha'bcmgyqz

		:NITSUERF|+
		;nitsuerf\=

		XVOD>KLP<J
		xvod.klp,j
	''')

	DELTA = stringToLayout(r'''
		~!@#$%^&*(){}
		`1234567890[]

		J+YUIMVAC>XQ?
		j=yuimvac.xq/

		BFHTOSERP"Z
		bfhtoserp'z

		:WGNKDL|<_
		;wgnkdl\,-
	''')

	EPSILON = stringToLayout(r'''
		~!@#$%^&*()_+
		`1234567890-=

		JKGPI?BAH"YZQ
		jkgpi/bah'yzq

		VCLTSDENMX\
		vcltsdenmx|

		W[UO<:RF>]
		w{uo,;rf.}
	''')

	THETA = stringToLayout(r'''
		~!@#$%^&*()_+
		`1234567890-=

		\XGC<FHI"BKJQ
		|xgc,fhi'bkjq

		VPOTLRENDWZ
		vpotlrendwz

		[Y>AMUS:?]
		{y.amus;/}
	''')

	# Candidate layout: Omega
	OMEGA = stringToLayout(r'''
		~!0123456789^
		`$[{(*/+)}]\%

		WFBMLGUIO_PQ@
		wfbmlguio-pq#

		NRSTDYEAH?|
		nrstdyeah=&

		ZXCVKJ"<>:
		zxcvkj',.;
	''')

	# Candidate layout: Omega old
	OMEGAOLD = stringToLayout(r'''
		~!0123456789^
		`$[{(*/+)}]\%

		WBLFDGUIO_PQ@
		wblfdguio-pq#

		NRSTMYEAH?|
		nrstmyeah=&

		ZXCVKJ"<>:
		zxcvkj',.;
	''')

	layouts = {
		'QWERTY': QWERTY,
		'DVORAK': DVORAK,
		'PDVORAK': PDVORAK,
		'COLEMAK': COLEMAK,
		'WORKMAN': WORKMAN,
		'ALPHA': ALPHA,
		'BETA': BETA,
		'GAMMA': GAMMA,
		'DELTA': DELTA,
		'EPSILON': EPSILON,
		'THETA': THETA,
		'OMEGA': OMEGA,
	}

	@staticmethod
	def displayLayout(layout):
		lines = []
		for i in range(len(layout)*3-1):
			line = []
			if i % 3 < 2:
				for thing in layout[i/3]:
					line.append(thing[i%3])
			lines.append(line)
		return '\n'.join(map(''.join, lines))

	@staticmethod
	def displayLayoutSimple(layout):
		return '\n'.join(''.join(x[1] for x in line) for line in layout[1:])

	stringToLayout = staticmethod(stringToLayout)

	@classmethod
	def typeCost(cls, layoutRow, layoutCol):
		return cls.keyCost[layoutRow][layoutCol]

	@classmethod
	@memo
	def bigramCost(cls, (row1, col1), (row2, col2)):
		layoutCol1 = cls.layoutColumnMap[row1][col1]
		finger1 = cls.fingerAssignment[layoutCol1]
		layoutCol2 = cls.layoutColumnMap[row2][col2]
		finger2 = cls.fingerAssignment[layoutCol2]
		if finger1 > finger2:
			finger1, finger2 = finger2, finger1 # we don't care about order of presses
			row1, row2 = row2, row1
			col1, col2 = col2, col1
			layoutCol1, layoutCol2 = layoutCol2, layoutCol1
		
		cost = cls.baseCost[finger1][0] + cls.baseCost[finger2][0]

		# add term corresponding to the stretching involved.  Multiply up cost if e.g. 1 finger apart but 2 cols apart?

		if finger1 == finger2: return 4. * cost # same finger
		if finger1 < 4 and finger2 >= 4: return 0.7 * cost # different hands
		
		# same hand. penalize difficult arrangements
		
		# make everything left-hand
		if finger1 >= 4:
			finger1 = 7 - finger1
			finger2 = 7 - finger2
		if finger1 > finger2:
			finger1, finger2 = finger2, finger1 # we don't care about order of presses
			row1, row2 = row2, row1
			col1, col2 = col2, col1
			layoutCol1, layoutCol2 = layoutCol2, layoutCol1

		if finger1 == 0 and finger2 == 3: return 1.5 * cost if abs(layoutCol1 - layoutCol2) < 4 else 3. * cost # not very nice if index and pinky
		if finger1 == 0:
			if row2 - row1 == 1: return 0.3 * cost
			if row2 == row1: return 0.5 * cost
			return 1.5 * cost if finger2 == 1 else 1. * cost
		if finger2 == 3:
			if row1 - row2 == 1: return 0.3 * cost
			if row1 == row2: return 0.5 * cost
			return 1. * cost
		# must be middle and ring finger now
		if row1 == row2: return 0.8 * cost
		if row2 - row1 == 1: return 1.2 * cost
		return 2. * cost

	@classmethod
	def bigramDebug(cls, R, C):
		print '\n'.join(
			' '.join(('%02.2f' % cls.bigramCost((R, C), (row, col))).rjust(5) if col >= 0 else ' '*5 for col in r)
			for row, r in enumerate([range(13), range(-1,13), range(-1,11), range(-1,10)]))

	@classmethod
	def costDebug(cls):
		print '\n'.join(
			' '.join(('%02.2f' % cls.typeCost(row,col)).rjust(5) if col >= 0 else ' '*5 for col in r)
			for row, r in enumerate([range(13), range(-1,13), range(-1,11), range(-1,10)]))

	def __init__(self, text):
		from ngrams import ngramCounts
		allowedCharacters = set(c for row in self.QWERTY for col in row for c in col) | set(' \t\n')
		text = ''.join(c for c in text if c in allowedCharacters)
		self.temperature = 0.0
		self.counts = ngramCounts(1, text)
		#print self.counts
		self.bigrams = ngramCounts(2, text)
		#print self.bigrams['ai'] + self.bigrams['ia']
		self.totalCharacters = sum(self.counts.values())
		self.characterWeighting = 1.0 / self.totalCharacters if self.totalCharacters != 0 else 0.0

		self.importantBigrams = sorted((count, bigram) for bigram, count in self.bigrams.items() if bigram[0] != bigram[1] and all(c not in bigram for c in ' \t\n'))[::-1][:4000]
		#print '\n'.join('%s %d' % (bigram, count) for count, bigram in self.importantBigrams)
		self.bigramWeighting = 1.0 / sum(count for count, bigram in self.importantBigrams)
	
	def __call__(self, layout, temperature):
		cells = [(row, col) for row in range(len(layout)) for col in range(len(layout[row]))]
		lookup = dict((c, (row, col)) for row, col in cells for c in layout[row][col])
		fingerWork = [0. for i in range(8)]
		for r, c in cells:
			fingerWork[self.fingerAssignment[self.layoutColumnMap[r][c]]] += self.typeCost(r, c) * (self.counts[layout[r][c][0]] + self.counts[layout[r][c][1]])
		return self.characterWeighting * sum(fingerWork) + temperature * 5. * self.characterWeighting * max(fingerWork) \
			+ temperature * 8. * self.bigramWeighting * sum(int(self.bigramCost(lookup[c1], lookup[c2]) * count) for count, (c1, c2) in self.importantBigrams) #\
			#+ 0.5 * sum(1. if self.fingerAssignment[self.layoutColumnMap[r][c]] < 4 else 0. for x in 'aeiou' for r, c in [lookup[x]]) # make vowels all on the right hand
			




if __name__ == '__main__':
	from sys import argv, stdin, stderr

	if len(argv) > 1:
		stderr.write('Invalid arguments given.  Usage: %s, to give average typing costs of known keyboard layouts on standard input.\n')
	else:
		model = TypingModel(stdin.read())
		for name, layout in model.layouts.items():
			print name, model(layout)


















