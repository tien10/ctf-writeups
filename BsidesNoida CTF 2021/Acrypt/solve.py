from z3 import *
def indentify_a_b():
	a = 0
	b = 0
	inp = [Int(f'inp{i}') for i in range(2)]
	s = Solver()
	s.add((37 * inp[0] + 0 + inp[1]) % 65 == 53)
	s.add((54 * inp[0] + 1 + inp[1]) % 65 == 18)
	if s.check() == sat:
		m = s.model()
		a = m[inp[0]].as_long()
		b = m[inp[1]].as_long()
		return [a, b]
		#for i in range(2):
		#	print(m[inp[i]].as_long())
#a = 17
#b = 529
if __name__ == '__main__':
	res = indentify_a_b()
	a = res[0]
	b = res[1]
	target 		= 'Ri}uXETL3fxnRXnCNHgVHJwwVzN6EGsYTeCg07LSr8y'
	alphabet 	= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'

	for i in range(0, len(target)):
		for j in range(0, len(alphabet)):
			tmp = (j*a + i + b) % 65
			if tmp == alphabet.find(target[i]):
				print(alphabet[j], end = '')
	print()