f = open('checkInput.c','r')
lines = f.read()

lines = lines.split('\n')
for i in range(0, len(lines)):
	tmp = lines[i]
	if '(unsigned __int8)' in tmp:
		tmp = tmp.replace('(unsigned __int8)', '0xff &')

	tmp = 's.add(' + tmp + ')' +'\n'
	lines[i] = tmp

res = ''
for line in lines:
	res += line

open('constraints.txt', 'w').write(res)