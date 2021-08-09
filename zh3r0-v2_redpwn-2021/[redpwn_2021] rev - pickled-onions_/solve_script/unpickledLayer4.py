import subprocess
def disAssemblyPKL(s):
	dataName 	= f'{s}.data'
	pklName		= f'{s}.pkl'

	subprocess.run(['python3', '-m', 'pickletools', f'./unpickled/data/{dataName}', '-o', f'./unpickled/pkl/{pklName}'])
	#print(pklName)
	f = open(f'./unpickled/pkl/{pklName}', 'r')
	lines = f.read()
	lines = lines.split('\n')
	name = 'init'
	preLine = ''
	for line in lines:
		if 'SHORT_BINUNICODE' in line:
			comp = line.split("'")				#comp[01] is function name
			name = comp[-2]
		elif 'SHORT_BINBYTES' in line or 'BINBYTES' in line:
			comp = line.split("b'")
			bytecode = comp[-1][:len(comp[-1]) - 1]			#delete "'" char at the end of string
			bytecode = 'I97\\n'*64 + bytecode
			bytecode = "b'" + bytecode + "'"		
			pickleData = eval(bytecode)			#convert "b'...'" to bytearray
			open(f'./unpickled/data/{name}.data', 'wb').write(pickleData)
			disAssemblyPKL(name)
		preLine = line
	return
if __name__ == '__main__':

	disAssemblyPKL('pickleLayer4')