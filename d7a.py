import csv
import copy

from itertools import permutations
combos = permutations([5,6,7,8,9])

# input from d5
#input = 5 

program = []

f = open("d7.txt")
for row in csv.reader(f):
	program = row

myprog = [int(i) for i in program]
#print(program)


#print('Program length = ',len(program))
#print('Initial value =',program[223])


def opcode(program,step,input,input2):
	i = step 
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
				#print('First input = ',input)
				program[out] = input 
			else:
				program[out] = input2
				#print('Second input = ',input2)
			i = i+2
		elif program[i] == 4:
			out = program[i+1]
			output = program[out]
			print('Output = ',output)
			return(output,program,i+2,0)
			break
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
			#print('HALT!!!!!!')
			return(0,program,i,1)
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
					print('First input = ',input)
				else:   
					program[program[i+1]] = input2
					print('Second input = ',input2)
				program[program[i+1]] = input
				i = i+2
			elif opcode == 4:
				out = program[i+1]
				print('output=',out)
				return(out,program,i+2,0)
				break
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
			elif opcode == 99:
				print('HALT!!!!!!')
				return(0,program,i,1)




progA = copy.deepcopy(myprog)
progB = copy.deepcopy(myprog)
progC = copy.deepcopy(myprog)
progD = copy.deepcopy(myprog)
progE = copy.deepcopy(myprog)

maxAmpE = 0 

#combos = [[9,8,7,6,5]]
firstiter = 0

for c in list(combos):
	print(c)
	initA = 0;
	firstiter = 0
	progA = copy.deepcopy(myprog)
	progB = copy.deepcopy(myprog)
	progC = copy.deepcopy(myprog)
	progD = copy.deepcopy(myprog)
	progE = copy.deepcopy(myprog)


	while True:
		if firstiter == 0:
			(ampA,progA,stepA,haltstate) = opcode(progA,0,c[0],initA)
			print('First Iteration: initA = ',initA,', AmpA = ',ampA,'haltstate = ',haltstate)
			#print(progA)
			(ampB,progB,stepB,haltstate) = opcode(progB,0,c[1],ampA)
			(ampC,progC,stepC,haltstate) = opcode(progC,0,c[2],ampB)
			(ampD,progD,stepD,haltstate) = opcode(progD,0,c[3],ampC)
			(ampE,progE,stepE,haltstate) = opcode(progE,0,c[4],ampD)
		else:
			(ampA,progA,stepA,haltstate) = opcode(progA,stepA,ampE,0) 
			#print('AmpA = ',ampA,'haltstate = ',haltstate)
			#print(progA)
			(ampB,progB,stepB,haltstate) = opcode(progB,stepB,ampA,0)
			(ampC,progC,stepC,haltstate) = opcode(progC,stepC,ampB,0)
			(ampD,progD,stepD,haltstate) = opcode(progD,stepD,ampC,0)
			(ampEt,progE,stepE,haltstate) = opcode(progE,stepE,ampD,0)
			if ampEt != 0:
				ampE = ampEt
			#print('progE = ',progE)
		firstiter = 1
		if haltstate == 1: break
		else: continue 
	if ampE > maxAmpE: maxAmpE = ampE

print(maxAmpE)






