from collections import Counter, deque

def ngrams(n, sequence):
	current = deque()
	iterator = iter(sequence)
	try:
		for i in range(n):
			current.append(iterator.next())
		while True:
			if all(isinstance(c, str) for c in current):
				yield ''.join(current)
			else:
				yield tuple(current)
			current.popleft()
			current.append(iterator.next())
	except StopIteration:
		return

def ngramCounts(n, sequence):
	return Counter(ngrams(n, sequence))


if __name__ == '__main__':
	from sys import argv, stdin, stderr

	invalidArguments = False
	if len(argv) != 2:
		invalidArguments = True
	else:
		try:
			n = int(argv[1])
			assert str(n) == argv[1]
		except:
			invalidArguments = True

	if invalidArguments:
		stderr.write('Invalid arguments given.  Usage: %s <n>, to give n-gram counts of standard input.\n')
	else:
		print repr(ngramCounts(n, (c for line in stdin for c in line)))
