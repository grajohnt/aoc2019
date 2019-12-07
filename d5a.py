import csv

# input from d5
input = 5 

program = []

f = open("d5.txt")
for row in csv.reader(f):
	program = row

program = [int(i) for i in program]
#print(program)
i = 0


print('Program length = ',len(program))
#print('Initial value =',program[223])


while True:
	print('			i=',i)
	#print(program[i])
	if program[i] == 1:
		in1 = program[i+1]
		in2 = program[i+2]
		out = program[i+3]
		program[out] = program[in1]+program[in2] 
		i = i+4
		#print(i)
	elif program[i] == 2:
		in1 = program[i+1]
		in2 = program[i+2]
		out = program[i+3]
		program[out] = program[in1]*program[in2]
		i = i+4
	elif program[i] == 3:
		out = program[i+1]
		program[out] = input 
		i = i+2
	elif program[i] == 4:
		out = program[i+1]
		output = program[out]
		print('Output = ',output)
		i = i+2
	elif program[i] == 5:
		if program[program[i+1]] != 0:
			i = program[program[i+2]]	
		else: i = i+3
	elif program[i] == 6:
		if program[program[i+1]] == 0:
			i = program[program[i+2]]
		else: i = i+3
	elif program[i] == 7:
		if program[program[i+1]] < program[program[i+2]]:
			program[program[i+3]] = 1
		else: program[program[i+3]] = 0	
		i = i+4
	elif program[i] == 8:
		if program[program[i+1]] == program[program[i+2]]:
			program[program[i+3]] = 1
		else: program[program[i+3]] = 0
		i = i+4
		
	elif program[i] == 99:
		break
	else:
		param = program[i]
		opcode = int(str(param)[-2:])
		print('		param=',param)
		if opcode == 1:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: 
				mode2 = int(str(param)[-4])
			except: 
				mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:
				in2 = program[i+2]
			out = program[i+3]
			program[out] = in1+in2
			print('		mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)
			i = i+4
		elif opcode == 2:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: mode2 = int(str(param)[-4])
			except: mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:
				in2 = program[i+2]
			out = program[i+3]
			print('		mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)
			program[out] = in1*in2
			i = i+4
		elif opcode == 3:
			program[program[i+1]] = input
			i = i+2
		elif opcode == 4:
			out = program[i+1]
			print('output=',out)
			i = i+2
		elif opcode == 5:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: mode2 = int(str(param)[-4])
			except: mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:	
				in2 = program[i+2]
			if in1 != 0:
				i = in2
			else: i = i+3 
			print('         mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)

		elif opcode == 6:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: mode2 = int(str(param)[-4])
			except: mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:
				in2 = program[i+2]
			if in1 == 0:
				i = in2
			else: i = i+3 
			print('         mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)

		elif opcode == 7:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: mode2 = int(str(param)[-4])
			except: mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:
				in2 = program[i+2]
			out = program[i+3]
			if in1 < in2:
				program[out] = 1
			else: program[out] = 0
			i = i+4
			print('         mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)

		elif opcode == 8:
			try: mode1 = int(str(param)[-3])
			except: mode1 = 0
			if mode1 == 0:
				in1 = program[program[i+1]]
			elif mode1 == 1:
				in1 = program[i+1]
			try: mode2 = int(str(param)[-4])
			except: mode2 = 0
			if mode2 == 0:
				in2 = program[program[i+2]]
			elif mode2 == 1:
				in2 = program[i+2]
			out = program[i+3]
			if in1 == in2:
				program[out] = 1
			else: program[out] = 0
			i = i+4
			print('         mode1=',mode1,' mode2=',mode2,'in1=',in1,' in2=',in2,' out=',out)




