from pwn import *

operation = {	'pickledhorseradish'		: ' + ',	\
				'pickledcoconut'			: ' - ',	\
				'pickledlychee'				: ' ^ ',	\
				'pickledcrabapple'			: ' == ',	\
				'pickledportabella'			: '!= ',	\
				'pickledquince'				: '<=',	\
				'pickledeasternmayhawthorn'	: '>='
			}


#một là 
#hoặc là tính toán kết quả giữa chúng và check kết quả với số thứ 3


def getPara(lines):
	para = [-1 for i in range(2)]
	index = [i for i in range(64)]
	stack = []
	for i in range(0, len(lines)):
		if 'POP' in lines[i]:
			stack.append(index[len(index) - 1])
			#index = index[i +1:]
			index = index[:len(index) - 1]
		elif 'PUT        1' in lines[i]:
			para[1] = index[len(index) - 1]

		elif 'PUT        0' in lines[i]:
			para[0] = index[len(index) - 1]
		if para[0] != -1 and para[1] != -1:
			return para

def getOperationFromType1(lines): 	
	#return ope
	operationLine = lines[146].split("'")
	comp = operationLine[-2].split(" ")
	return operation[comp[-1]]

def getOperationFromType2(lines):	
	#return ope1, third operand, ope2
	ope1 = ''
	ope2 = ''
	thirdOperand = ''


	operation1Line = lines[149].split("'")[-2]			#  538: c        GLOBAL     'io pickledcoconut'
	comp = operation1Line.split(" ")					#io pickledcoconut
	ope1 = operation[comp[-1]]

	thirdOperandLine = lines[153]							#  576: I        INT        68
	num = [x for x in thirdOperandLine.split() if x.isdigit() == True]
	thirdOperand = num[0]

	operation2Line = lines[158].split("'")[-2]						#  597: c    GLOBAL     'io pickledcrabapple'
	comp = operation2Line.split(" ")
	ope2 = operation[comp[-1]]
	return [ope1, thirdOperand, ope2]
allConstraints = ''
type1 = []
type2 = []
notype = []
def getConstraints(func):				#get constraints for z3 solver()
	global allConstraints
#line 139: next function
#constraintType:
#type1: so sánh hai toán hạng với nhau
			#lines[146] operation, vd:   503: c    GLOBAL     'io pickledquince'

#type2: tính toán kết quả giữa chúng và check kết quả với số thứ 3()
			#line[149] operation1, line[152] third operand, line[158] operation2
	nameNextFunc= "init"
	if func == 'pickledmonstera':
		return
	pklFile = open(f'./unpickled/pkl/{func}.pkl', 'r')
	lines = pklFile.read().split('\n')
	#lines = lines[:len(lines) - 1]
	if len(lines) == 157 or len(lines) == 169:
		nameNextFunc = lines[138].split("'")[-2]
		indexInput = getPara(lines)

		#print('inp[', indexInput[0],'], inp[',indexInput[1], ']' )
		if len(lines) == 157:
			#type1.append(func)
			operate = getOperationFromType1(lines)
			constraint = 's.add(' + 'inp[' + str(indexInput[0]) + '] ' +  operate + ' inp[' + str(indexInput[1]) + '])'
			allConstraints += constraint + '\n'
		elif len(lines) == 169:
			operate = getOperationFromType2(lines)
			ope1 = operate[0]
			thirdOperand = operate[1]
			ope2 = operate[2]
			constraint = 's.add(' + 'inp[' + str(indexInput[0]) + '] ' +  ope1 + ' inp[' + str(indexInput[1]) + '] ' + ope2+ str(thirdOperand)+ ')'
			
			allConstraints += constraint + '\n'
		getConstraints(nameNextFunc)
		
			#type2.append(func)
	#else:
		#notype.append(func)
	return 
	#getConstraints()
	#for line in lines:
	#	print(line)




if __name__ == '__main__':
	getConstraints('pickledvoavanga')
	#print(len(type1))		#cac ham gom 2 toan hang
	#print(len(type2))		#cac ham gom 2 toan hang va toan hang thu 3
	#print(len(notype))		#check xem co ham nao ngoai le ko?
	#print('\n\n\n')
	#getConstraints('pickledacai')	
	open('ConstraintInputZ3.txt', 'w').write(allConstraints)

