import subprocess
def getPickleLayer2():
	layer1 = open('pickled-onions.py','r')
	pickleDataLayer2 = eval(layer1.read()[27:-1])		#read b'(I128\\nI4\\n...5R\\x85R.'
	open('pickleLayer2.data', 'wb').write(pickleDataLayer2)
	subprocess.run(['python3', '-m', 'pickletools','pickleLayer2.data', '-o', 'pickleLayer2.pkl'])
	return

def getPickleLayer3():
	layer2 = open('pickleLayer2.pkl', 'r')
	lines = layer2.read()
	lines = lines.split('\n')
	pickleDataLayer3 = []
	for line in lines:
		if "I        INT        " in line:
			number = [int(s) for s in line.split() if s.isdigit() == True]
			pickleDataLayer3.extend(number)

	pickleDataLayer3 = bytearray(pickleDataLayer3)
	open('pickleLayer3.data', 'wb').write(pickleDataLayer3)
	subprocess.run(['python3', '-m', 'pickletools', 'pickleLayer3.data', '-o', 'pickleLayer3.pkl'])
	return
def getPickleLayer4():
	layer3 = open('pickleLayer3.pkl', 'r')
	lines = layer3.read()
	lines = lines.split('\n')
	#print(lines)
	pickleDataLayer4 = ''
	for line in lines:
		if 'B        BINBYTES   ' in line:
			pickleDataLayer4 += line[27:len(line)]
	open('pickleLayer4.data', 'wb').write(eval(pickleDataLayer4))
	subprocess.run(['python3', '-m', 'pickletools', 'pickleLayer4.data', '-o', 'pickleLayer4.pkl'])
	return


if __name__ == '__main__':
	getPickleLayer2()
	getPickleLayer3()
	getPickleLayer4()
