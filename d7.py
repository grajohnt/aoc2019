import csv
import copy

from itertools import permutations
combos = permutations([0,1,2,3,4])

# input from d5
#input = 5 

program = []

f = open("d7.txt")
for row in csv.reader(f):
	program = row

program = [int(i) for i in program]
#print(program)


#print('Program length = ',len(program))
#print('Initial value =',program[223])


def opcode(program,input,input2):
	i = 0
	ic = 0
	while True:
		#print('			i=',i)
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
			# Add trap for second input (also below)
			ic = ic + 1
			out = program[i+1]
			if ic == 1:	
				program[out] = input 
			else:   program[out] = input2
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
			return output
			break
		else:
			param = program[i]
			opcode = int(str(param)[-2:])
			#print('		param=',param)
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
				program[out] = in1*in2
				i = i+4
			elif opcode == 3:
				ic = ic + 1
				if ic == 1:     
					program[program[i+1]] = input
				else:   program[program[i+1]] = input2
	
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



progA = copy.copy(program)
progB = copy.copy(program)
progC = copy.copy(program)
progD = copy.copy(program)
progE = copy.copy(program)

maxAmpE = 0 

for c in list(combos):
	print(c)
	ampA = opcode(progA,c[0],0)
	print('AmpA = ',ampA)
	ampB = opcode(progB,c[1],ampA)
	print('AmpB = ',ampB)
	ampC = opcode(progC,c[2],ampB)
	print('AmpC = ',ampC)
	ampD = opcode(progD,c[3],ampC)
	print('AmpD = ',ampD)
	ampE = opcode(progE,c[4],ampD)
	print('AmpE = ',ampE)
	if ampE > maxAmpE: maxAmpE = ampE

print(maxAmpE)






