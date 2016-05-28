from random import randint, choice, random, sample
import math
import time
from model import Model, Layouts


def mutateLayout(layout, temperature, unfrozenCells = None):
	result = list(list(thing) for thing in layout)

	# Just randomly transpose some cells.
	while True:
		if unfrozenCells is None:
			r1 = randint(0, len(layout) - 1)
			r2 = randint(0, len(layout) - 1)
			c1 = randint(0, len(layout[r1]) - 1)
			c2 = randint(0, len(layout[r2]) - 2)
		else:
			(r1, c1), (r2, c2) = sample(unfrozenCells, 2)
		
		result[r1][c1], result[r2][c2] = result[r2][c2], result[r1][c1]

		# Transpose a random number of times.
		if random() > 3. / 4.:
			break

	return result

def annealLayout(layout, cost, model, temperature, unfrozenCells = None, bestKnownCost = None):

	# Mutation mutates more when at high temperatures.
	neighbour = mutateLayout(layout, temperature, unfrozenCells)

	# We just perform a Metropolis-Hastings step with the specified temperature.
	
	# As a further point of help, if the bestKnownCost is around, we can transform the energy landscape to make it easier to tunnel
	# through walls above the best known cost.
	def transformedCost(c):
		return c if bestKnownCost is None else bestKnownCost + (c - bestKnownCost) * (0.1 if c > bestKnownCost else 2)

	neighbourCost = model(neighbour)
	if neighbourCost < cost:
		#if randint(0, 1000) == 0:
		#	print "T:", 1
		#	print neighbourCost
		return neighbour, neighbourCost
	else:
		transitionProbability = math.exp((transformedCost(cost) - transformedCost(neighbourCost)) / (0.000001 + temperature))
		#if randint(0, 1000) == 0:
		#	print "T:", transitionProbability
		#	print neighbourCost
		if random() < transitionProbability:
			return neighbour, neighbourCost
		else:
			return layout, cost

def searchForCandidateLayout(layout, cost, model, iterations, initialTemperatureExponent, unfrozenCells = None):
	bestLayout = layout
	bestCost = cost

	for i in range(iterations):
		temperature = math.exp(-initialTemperatureExponent - max(8. - initialTemperatureExponent, 1.) * i / iterations)
		layout, cost = annealLayout(layout, cost, model, temperature, unfrozenCells=unfrozenCells, bestKnownCost=bestCost)
		
		if cost < bestCost:
			bestLayout, bestCost = layout, cost

	return tuple(tuple(thing) for thing in bestLayout), bestCost

def searchForCandidateLayouts(layout, cost, model, iterations = 15, results = 1, unfrozenCells = None):
	if iterations < 2 * results:
		iterations = 2 * results

	candidates = set([(layout, cost)])

	for i in range(iterations):
		layout, cost = choice(list(candidates))
		candidates.add(searchForCandidateLayout(layout, cost, model, 5000 + 10000 * i / iterations, 3. + 2. * i / iterations, unfrozenCells = unfrozenCells))

		if len(candidates) * 2 > i + 7:
			candidates.remove(min(candidates, key = lambda (layout, cost): cost))

	return list(sorted(candidates, key = lambda (layout, cost): cost))[:results]


def optimizeLayout(layout, model, unfrozenCells = None, processes = 8):
	candidates = ((layout, model(layout)),)

	from multiprocessing import Pool
	processPool = Pool(processes = processes)
	try:
		iterations = (24 + processes - 1) / processes
		for i in range(iterations):
			print '%.1f%% (%d/%d iterations)' % (i * 100. / iterations, i, iterations)
			candidates = tuple(set(processPool.map(lambda (layout, cost): searchForCandidateLayouts(layout, cost, model, unfrozenCells = unfrozenCells)[0], [min(candidates, key = lambda (layout, cost): cost)] * ((processes + 1) / 2) + [choice(candidates) for i in range(processes - (processes+1)/2)])))
			print 'Candidate costs:', ', '.join(map(lambda cost: '%.4f' % cost, sorted(cost for layout, cost in candidates)))
		return min(candidates, key = lambda (layout, cost): cost)
	finally:
		processPool.terminate()



def main():
	from sys import argv, stdin

	if len(argv) == 1 or argv[1] != '-':
		print "Loading saved model...",
		model = Model.load('model' if len(argv) == 1 else argv[1])
		print "Done."
	else:
		print "Building model from text on standard input...",
		model = Model(stdin.read())
		print "Done."
		return

	def show(layout, cost):
		print "Cost:", cost
		print
		print Model.displayLayout(layout)
		print
		print

	seed = Layouts.OMEGA3

	#((0, len(seed[0]) - 1),)

	unfrozenCells = tuple() + \
					tuple((1, c) for c in range(len(seed[1]) - 3)) + \
					tuple((2, c) for c in range(len(seed[2]))) + \
					tuple((3, c) for c in range(len(seed[3])))
					#tuple((3, c) for c in range(4, len(seed[3]) - 2))
	
	show(seed, model(seed))

	global results1, results2, results3, results4
	results1 = []
	results2 = []
	results3 = []
	results4 = []

	for attempt in range(10):
		for simplicity in (0.0,):
			print
			print '----------------------'
			print 'simplicity = %.1f' % simplicity
			print '----------------------'

			startTime = time.time()

			for i in range(20):
				seed, _ = annealLayout(seed, model(seed), model, temperature = 1.0, unfrozenCells = unfrozenCells)
			seed = tuple(tuple(thing for thing in row) for row in seed)

			seed, cost = optimizeLayout(seed, lambda layout: model(layout, simplicity = simplicity), unfrozenCells = unfrozenCells)
			show(seed, cost)

			if simplicity == 0.0:
				results1.append((seed, cost))

			print
			print '[time: %s]' % (time.time() - startTime)
			print '----------------------'

	for attempt in range(10):
		for simplicity in (0.01, 0.0):
			print
			print '----------------------'
			print 'simplicity = %.1f' % simplicity
			print '----------------------'

			startTime = time.time()

			for i in range(20):
				seed, _ = annealLayout(seed, model(seed), model, temperature = 1.0, unfrozenCells = unfrozenCells)
			seed = tuple(tuple(thing for thing in row) for row in seed)

			seed, cost = optimizeLayout(seed, lambda layout: model(layout, simplicity = simplicity), unfrozenCells = unfrozenCells)
			show(seed, cost)

			if simplicity == 0.0:
				results2.append((seed, cost))

			print
			print '[time: %s]' % (time.time() - startTime)
			print '----------------------'

	for attempt in range(10):
		for simplicity in (0.8, 0.0,):
			print
			print '----------------------'
			print 'simplicity = %.1f' % simplicity
			print '----------------------'

			startTime = time.time()

			for i in range(20):
				seed, _ = annealLayout(seed, model(seed), model, temperature = 1.0, unfrozenCells = unfrozenCells)
			seed = tuple(tuple(thing for thing in row) for row in seed)

			seed, cost = optimizeLayout(seed, lambda layout: model(layout, simplicity = simplicity), unfrozenCells = unfrozenCells)
			show(seed, cost)

			if simplicity == 0.0:
				results3.append((seed, cost))

			print
			print '[time: %s]' % (time.time() - startTime)
			print '----------------------'

	for attempt in range(10):
		for simplicity in (1.0, 0.8, 0.3, 0.0):
			print
			print '----------------------'
			print 'simplicity = %.1f' % simplicity
			print '----------------------'

			startTime = time.time()

			for i in range(20):
				seed, _ = annealLayout(seed, model(seed), model, temperature = 1.0, unfrozenCells = unfrozenCells)
			seed = tuple(tuple(thing for thing in row) for row in seed)

			seed, cost = optimizeLayout(seed, lambda layout: model(layout, simplicity = simplicity), unfrozenCells = unfrozenCells)
			show(seed, cost)

			if simplicity == 0.0:
				results4.append((seed, cost))

			print
			print '[time: %s]' % (time.time() - startTime)
			print '----------------------'

	print "1:", ', '.join('%.3f' % cost for layout, cost in results1)
	print "2:", ', '.join('%.3f' % cost for layout, cost in results2)
	print "3:", ', '.join('%.3f' % cost for layout, cost in results3)
	print "4:", ', '.join('%.3f' % cost for layout, cost in results4)


if __name__ == '__main__':
	main()
