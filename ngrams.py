from collections import Counter, deque

def ngrams(n, sequence):
	if isinstance(sequence, str):
		for i in range(len(sequence)-n):
			yield sequence[i:i+n]
	else:
		current = deque()
		iterator = iter(sequence)
		try:
			for i in range(n):
				current.append(iterator.next())
			while True:
				yield tuple(current)
				current.popleft()
				current.append(iterator.next())
		except StopIteration:
			return

def ngramCounts(n, sequence):
	return Counter(map(''.join, ngrams(n, sequence))) if isinstance(sequence, str) else Counter(ngrams(n, sequence))



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
		print repr(ngramCounts(n, stdin.read()))
