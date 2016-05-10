from sys import stdin
from random import randint, choice
from model import TypingModel

def evolve(seeds, score, spawn, optimize, lowTemp = 0., highTemp = 1., processPool=None, results=5, children=50, population=500, iterations = 50):
	pool = list(reversed(sorted((score(seed, 0.0), seed) for seed in seeds)))

	best = pool[-1]

	mapper = map if processPool is None else processPool.map

	for i in range(iterations):
		newPool = []
		fertility = children
		temp = lowTemp + (highTemp - lowTemp) * i * 1. / iterations

		newPop = 0
		todo = []
		while pool and newPop < population:
			_, seed = pool.pop()
			for x in range(3): todo.append((seed, fertility/3))
			newPop += fertility
			fertility = max(fertility * 2 / 3, 6)

		# Temp: no optimize
		#todo = list(mapper(lambda (seed, number): (optimize(lambda l: score(l, temp), seed), number), todo))
		offspring = list(mapper(lambda (seed, number): [spawn(seed) for i in range(number)], todo))

		for group in offspring:
			newPool.extend(group)

		newPool = list(mapper(lambda layout: (score(layout, temp), layout), newPool))
		newPool.sort(key=lambda (score, layout): score)
		pool = newPool[::-1]

		if (i % 5) == 0:
			print 'Iteration %3d: %.2f, %.2f, %.2f, %.2f, %.2f, %.2f' % (i, newPool[0][0], newPool[1][0], newPool[2][0], newPool[3][0], newPool[10][0], newPool[50][0] if len(newPool) > 50 else float('+inf'))

		if False and (i % 100) == 0 and i > 0:
			print '------------------------------'
			print
			print TypingModel.displayLayoutSimple(newPool[0][1])
			print
			print '------------------------------'
			print
			print TypingModel.displayLayoutSimple(newPool[1][1])
			print
			print '------------------------------'
			__import__('sys').stdin.flush()

		if False and newPool[0][0] < best[0]:
			best = newPool[0]
			print
			print "New best: ", best[0]
			print '~~~~~~~~~~~~~~~~~~~~'
			print TypingModel.displayLayoutSimple(best[1])
			print '~~~~~~~~~~~~~~~~~~~~'
			print

	return [layout for score, layout in newPool[:results]]


def main():
	seedA = TypingModel.stringToLayout(r'''
		~$0123456789^
		`*/{[(=+)]}\%

		"_FRLDTIOBQ|@
		'-frldtiobq&#

		:USNHPMEAGY
		;usnhpmeagy

		ZXCVWJK<>?
		zxcvwjk,.!
	''')

	seed = TypingModel.stringToLayout(r'''
		~$0123456789^
		`*/{[(=+)]}\%

		_YFRLDTUIPQ|@
		-yfrldtuipq&#

		BGSNHMOEA:"
		bgsnhmoea;'

		ZXCVWJK<>?
		zxcvwjk,.!
	''')


	# seeds = list(TypingModel.layouts.values())

	firstRow = 1
	lastRow = 2
	firstCol = (0, 1, 0, 0)
	lastCol = (len(seed[0])-1, len(seed[1])-1-3, len(seed[2])-1-0, len(seed[3])-1-0)
	firstFreeRow = 1
	lastFreeRow = 2

	if len(__import__('sys').argv) > 1:
		print "Building model from text on standard input...",
		model = TypingModel(stdin.read())
		import cPickle
		with open('model.pickle', 'w') as f:
			cPickle.dump(model, f)
		print "Done."
		return
	else:
		print "Loading saved model...",
		import cPickle
		model = cPickle.load(open('model.pickle'))
		print "Done."


	lay1 = TypingModel.stringToLayout('''
		~$0123456789^
		`*/{[(=+)]}\%

		_DLNUMTEABQ|@
		-dlnumteabq&#

		YSRHPGFIO:"
		ysrhpgfio;'

		ZXCVWJK<>?
		zxcvwjk,.!
	''')


	lay2 = TypingModel.stringToLayout('''
		~$0123456789^
		`*/{[(=+)]}\%

		_"LUYMDIABQ@|
		-'luymdiabq#&

		FRSNHGTEOP:
		frsnhgteop;

		ZXCVWJK<>?
		zxcvwjk,.!
	''')


	#print model(lay1, 1.), model(lay2, 1.)
	#for name, l in model.layouts.items():
	#	print name, model(l, 1.)
	#return


	def mutateLayout(layout):
		
		#if randint(0,5000) == 0:
		#	return choice(TypingModel.layouts.values())

		def doMutate(l):
			op = 3 #randint(0,10)
			if op == 0:
				row = randint(firstFreeRow, lastFreeRow)
				move = randint(1,4)
				l[row] = l[row][move:] + l[row][:move]
			elif op == 1:
				row = randint(firstFreeRow, lastFreeRow)
				move = randint(-4,-1)
				l[row] = l[row][move:] + l[row][:move]
			elif op == 2:
				r1 = randint(firstFreeRow, lastFreeRow)
				r2 = r1-1 if r1 > 1 else 2
				c1, c2 = randint(0, min(len(l[r1]), len(l[r2]))), randint(0, min(len(l[r1]), len(l[r2])))
				if c1 > c2: c1, c2 = c2, c1
				if c1 == c2: c1 = max(c1 - 1, 0); c2 = min(len(l[r1]), len(l[r2]))
				for c in range(c1, c2):
					l[r1][c], l[r2][c] = l[r2][c], l[r1][c]
			else:
				r1, r2 = randint(firstRow, lastRow), randint(firstRow, lastRow)
				c1, c2 = randint(firstCol[r1], lastCol[r1]), randint(firstCol[r2], lastCol[r2])
				l[r1][c1], l[r2][c2] = l[r2][c2], l[r1][c1]


			if randint(0,15) > 0:
				doMutate(l)

		result = list(list(thing) for thing in layout)
		doMutate(result)
		return result

	def optimizeLayout(score, layout):
		return layout
		# TEMP: does this make things better overall?

		layout = [[x for x in l] for l in layout]
		success = True
		current = score(layout)
		while success:
			success = False
			for i in range(20):
				row1 = randint(firstRow, lastRow)
				col1 = randint(firstCol[row1], lastCol[row1])
				row2 = randint(firstRow, lastRow)
				col2 = randint(firstCol[row2], lastCol[row2])
				layout[row1][col1], layout[row2][col2] = layout[row2][col2], layout[row1][col1]
				nextScore = score(layout)
				if nextScore < current:
					current = nextScore
					success = True
				else:
					layout[row1][col1], layout[row2][col2] = layout[row2][col2], layout[row1][col1]
		return layout


	results = [seed] #[seed, seedA]
	from results import keyboards#, preliminaryKeyboards
	results = keyboards
	#results = [lay2]
	#results = preliminaryKeyboards

	cycles = 40
	steps = 15
	iterations = 16

	population = 1200
	children = population / 20

	from multiprocessing import Pool
	pool = Pool(processes=8)

	import random

	for cycle in range(cycles):
		print
		print "~~~~~~~~~~~~~~~~~"
		print "Cycle %d of %d..." % (cycle + 1, cycles)
		print "~~~~~~~~~~~~~~~~~"
		print
		for step in range(steps):
			print "============================"
			print "Step %d of %d..." % (step + 1, steps)
			print "============================"
			print

			minTemp = (step * 0.8 / steps) * (1. - cycle * 1./cycles) + cycle * 1./cycles
			maxTemp = ((step + 1) * 0.8 / steps + 0.2) * (1. - cycle * 1./cycles) + cycle * 1./cycles
			seed, = evolve([random.choice(results)], model, mutateLayout, optimizeLayout, minTemp, maxTemp, processPool=pool, results=1, children=children, population=population, iterations=iterations)

			print
			print '============================'
			print
			print TypingModel.displayLayout(seed)
			print
			print '============================'
			print

		results.append(seed)

	print '~~~~~~~~'
	print 'Results:'
	print '~~~~~~~~'
	print
	for layout in results:
		print '============================'
		print
		print TypingModel.displayLayout(layout)
		print
		print '============================'
		print

	print
	print '~~~~~~~~~~~~~~~~~~~~~'
	print 'Final optimization...'
	print '~~~~~~~~~~~~~~~~~~~~~'
	print

	final = dict()
	for seed in dict((TypingModel.displayLayout(l), l) for l in results).values():
		layout, = evolve([seed], model, mutateLayout, optimizeLayout, 1., 1., processPool=pool, results=1, children=1000, population=15000, iterations=11)
		print
		print TypingModel.displayLayout(layout)
		print
		print "========================================"
		print
		final[TypingModel.displayLayout(layout)] = layout

	print
	print '~~~~~~~~~~~~~~~~'
	print 'Final results...'
	print '~~~~~~~~~~~~~~~~'
	for s, l in sorted((model(l, 1.), l) for l in final.values()):
		print
		print '# score = %.4f' % s
		print "'''"
		print TypingModel.displayLayout(l)
		print "''',"

if __name__ == '__main__':
	main()
