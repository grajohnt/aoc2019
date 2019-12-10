import csv
import copy

#from itertools import permutations
#combos = permutations([5,6,7,8,9])

# input from d5
#input = 5 

program = []

debug = 0 

f = open("d9a.txt")
for row in csv.reader(f):
	program = row


myprog = [int(i) for i in program]
myprog.extend([0] * 2000)
#print(myprog)


#print('Program length = ',len(program))
#print('Initial value =',program[223])


def opcode(program,step,input,input2):
	i = step 
	ic = 0
	# define new relative base
	rb = 0

	while True:
		#print('			i=',i)
		if debug==1: print('Step: ',i,' Command: ',program[i], ' Relative Base: ',rb)
		if program[i] == 1:
			in1 = program[i+1]
			in2 = program[i+2]
			out = program[i+3]
			if debug==1: print('inaddr = ',in1,' inaddr2 = ',in2,' outaddr = ',out)
			program[out] = program[in1]+program[in2] 
			i = i+4
			#print(i)
		elif program[i] == 2:
			in1 = program[i+1]
			in2 = program[i+2]
			out = program[i+3]
			program[out] = program[in1]*program[in2]
			if debug==1: print('inaddr = ',in1,' inaddr2 = ',in2,' outaddr = ',out)
			i = i+4
		elif program[i] == 3:
			# Add trap for second input (also below)
			#ic = ic + 1
			out = program[i+1]
			if debug==1: print('Inputting value =',input)
			#if ic == 1:	
				#print('First input = ',input)
			#	program[out] = input 
			#else:
		#		program[out] = input2
				#print('Second input = ',input2)
			i = i+2
		elif program[i] == 4:
			out = program[i+1]
			output = program[out]
			print('						Output = ',output)
			#return(output,program,i+2,0)
			#break
			i = i+2
		elif program[i] == 5:
			if program[program[i+1]] != 0:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'ne 0 - setting i to ',program[program[i+2]])
				i = program[program[i+2]]	
			else: 
				i = i+3
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'= 0 no action')
		elif program[i] == 6:
			if program[program[i+1]] == 0:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'= 0 - setting i to ',program[program[i+2]])
				i = program[program[i+2]]
			else:
				i = i+3
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'ne 0 no action')
		elif program[i] == 7:
			if program[program[i+1]] < program[program[i+2]]:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'< Address',program[i+2],' =',program[program[i+2]],'setting address ',program[i+3],' to 1') 
				program[program[i+3]] = 1
			else:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'!< Address',program[i+2],' =',program[program[i+2]],'setting address ',program[i+3],' to 0')
				program[program[i+3]] = 0	
			i = i+4
		elif program[i] == 8:
			if program[program[i+1]] == program[program[i+2]]:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'== Address',program[i+2],' =',program[program[i+2]],'setting address ',program[i+3],' to 1')
				program[program[i+3]] = 1
			else:
				if debug==1: print('Address ',program[i+1],'=',program[program[i+1]],'!= Address',program[i+2],' =',program[program[i+2]],'setting address ',program[i+3],' to 0')
				program[program[i+3]] = 0
			i = i+4
			
		elif program[i] == 9:
			if debug==1: print('Setting rb of ',rb,'to ',rb,'+',program[program[i+1]],'=',rb+program[program[i+1]])
			rb = rb + program[program[i+1]]
			i = i+2
		elif program[i] == 99:
			if debug==1: print('HALT!!!!!!')
			return(0,program,i,1)
			break
		else:
			param = program[i]
			opcode = int(str(param)[-2:])
			#print('				param=',param)
			if opcode == 1:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					in1 = program[program[i+1]]
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
				elif mode1 == 1:
					in1 = program[i+1]
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
				elif mode1 == 2:
					in1 = program[rb+program[i+1]]
					if debug==1: print('Mode 2: address ',rb+program[i+1],'=',program[rb+program[i+1]])
				try: 
					mode2 = int(str(param)[-4])
				except: 
					mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:
					in2 = program[i+2]
					if debug==1: print('Mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				#out = program[i+3]
				try: mode3 = int(str(param)[-5])
				except: mode3 = 0
				if mode3 == 0:
					out = program[i+3]
				elif mode3 == 1:
					out = i+3
				elif mode3 == 2:
					out = rb+program[i+3]
				program[out] = in1+in2
				if debug==1: print('Add: setting ',program[out],' = ',in1,'+','in2','=',in1+in2)
				i = i+4
			elif opcode == 2:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					in1 = program[program[i+1]]
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
				elif mode1 == 1:
					in1 = program[i+1]
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
				elif mode1 == 2:
					in1 = program[rb+program[i+1]]
					if debug==1: print('Mode 2: address ',rb+program[i+1],'=',program[rb+program[i+1]])
				try: mode2 = int(str(param)[-4])
				except: mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:
					in2 = program[i+2]
					if debug==1: print('Mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				#out = program[i+3]
				try: mode3 = int(str(param)[-5])
				except: mode3 = 0
				if mode3 == 0:
					out = program[i+3]
				elif mode3 == 1:
					out = i+3
				elif mode3 == 2:
					out = rb+program[i+3]

				program[out] = in1*in2
				if debug==1: print('Multply: setting address',out,' = ',in1,'*',in2,'=',in1*in2)
				i = i+4
			elif opcode == 3:
				#ic = ic + 1
				#if ic == 1:     
				#	program[program[i+1]] = input
				#	print('First input = ',input)
				#else:   
				#	program[program[i+1]] = input2
				#	print('Second input = ',input2)
				#program[program[i+1]] = input
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					program[program[i+1]] = input
					if debug==1: print('Input mode 0: ',input,'going to ',program[i+1]) 
				elif mode1 == 1:
					program[i+1] = input
					if debug==1: print('Input mode 1: ',input,'going to ',i+1)
				elif mode1 == 2:
					program[rb+program[i+1]] = input
					if debug==1: print('Input mode 2: ',input,'going to ',rb+program[i+1])
				i = i+2
			elif opcode == 4:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					out = program[program[i+1]]
					if debug==1: print('Output mode 0: address ',program[program[i+1]])
				elif mode1 == 1:
					out = program[i+1]
					if debug==1: print('Output mode 1: address ',program[i+1])
				elif mode1 == 2:
					out = program[rb+program[i+1]]                    
					if debug==1: print('Output mode 2: address ',program[rb+program[i+1]])
				#out = program[i+1]
				print('output=',out)
				#return(out,program,i+2,0)
				#break
				i = i+2
			elif opcode == 5:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
					in1 = program[program[i+1]]
				elif mode1 == 1:
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
					in1 = program[i+1]
				elif mode1 == 2:
					if debug==1: print('Mode 2: address ',rb+program[i+1],'= ',program[rb+program[i+1]])
					in1 = program[rb+program[i+1]]                    
				try: mode2 = int(str(param)[-4])
				except: mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:	
					in2 = program[i+2]
					if debug==1: print('mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]                    
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				if in1 != 0:
					if debug==1: print(in1,' not == 0 - Jump to ',in2)
					i = in2
				else:
					if debug==1: print(in1,' == 0 - no jump')
					i = i+3 

			elif opcode == 6:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					in1 = program[program[i+1]]
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
				elif mode1 == 1:
					in1 = program[i+1]
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
				elif mode1 == 2:
					in1 = program[rb+program[i+1]]                    
					if debug==1: print('Mode 2: address ',rb+program[i+1],'= ',program[rb+program[i+1]])
				try: mode2 = int(str(param)[-4])
				except: mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:
					in2 = program[i+2]
					if debug==1: print('Mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]                    
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				if in1 == 0:
					if debug==1: print('Equals 0 - Jump to ',in2)
					i = in2
				else:
					if debug==1: print('Not equal 0 - no jump')
					i = i+3 

			elif opcode == 7:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
					in1 = program[program[i+1]]
				elif mode1 == 1:
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
					in1 = program[i+1]
				elif mode1 == 2:
					in1 = program[rb+program[i+1]]                   
					if debug==1: print('Mode 2: address ',rb+program[i+1],'= ',program[rb+program[i+1]])
				try: mode2 = int(str(param)[-4])
				except: mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:
					in2 = program[i+2]
					if debug==1: print('Mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]                                        
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				try: mode3 = int(str(param)[-5])
				except: mode3 = 0
				if mode3 == 0:
					out = program[i+3]
				elif mode3 == 1:
					out = i+3
				elif mode3 == 2:
					out = rb+program[i+3]
				#out = program[i+3]
				if in1 < in2:
					program[out] = 1
					if debug==1: print(in1,' < ',in2,' set ',out,' to 1')
				else:
					program[out] = 0
					if debug==1: print(in1,' !< ',in2,' set ',out,' to 0')
				i = i+4

			elif opcode == 8:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					in1 = program[program[i+1]]
					if debug==1: print('Mode 0: address ',program[i+1],'= ',program[program[i+1]])
				elif mode1 == 1:
					in1 = program[i+1]
					if debug==1: print('Mode 1: address ',i+1,'= ',program[i+1])
				elif mode1 == 2:
					in1 = program[rb+program[i+1]]                    
					if debug==1: print('Mode 2: address ',rb+program[i+1],'= ',program[rb+program[i+1]])
				try: mode2 = int(str(param)[-4])
				except: mode2 = 0
				if mode2 == 0:
					in2 = program[program[i+2]]
					if debug==1: print('Mode 0: address ',program[i+2],'= ',program[program[i+2]])
				elif mode2 == 1:
					in2 = program[i+2]
					if debug==1: print('Mode 1: address ',i+2,'= ',program[i+2])
				elif mode2 == 2:
					in2 = program[rb+program[i+2]]                                        
					if debug==1: print('Mode 2: address ',rb+program[i+2],'= ',program[rb+program[i+2]])
				#out = program[i+3]
				try: mode3 = int(str(param)[-5])
				except: mode3 = 0
				if mode3 == 0:
					out = program[i+3]
				elif mode3 == 1:
					out = i+3
				elif mode3 == 2:
					out = rb+program[i+3]
				if in1 == in2:
					program[out] = 1
					if debug==1: print(in1,' == ',in2,' set ',out,' to 1')
				else: 
					program[out] = 0
					if debug==1: print(in1,' != ',in2,' set ',out,' to 0')	
				i = i+4
			elif opcode == 9:
				try: mode1 = int(str(param)[-3])
				except: mode1 = 0
				if mode1 == 0:
					rbval = program[program[i+1]]
					if debug==1: print('Mode 0: Rel Base from address ',program[i+1],' is ',program[program[i+1]])
				elif mode1 == 1:
					rbval = program[i+1]
					if debug==1: print('Mode 1: Rel Base from address ',i+1,' is ',program[i+1])
				elif mode1 == 2:
					rbval = program[rb+program[i+1]]                    
					if debug==1: print('Mode 2: Rel Base from address ',rb+program[i+1],' is ',program[rb+program[i+1]])
				if debug == 1: print('Setting rb to ',rb,' + ',rbval)
				rb = rb + rbval
				#rb = rb + program[i+1]
				#print('rb = ',rb)
				i = i+2
			elif opcode == 99:
				print('HALT!!!!!!')
				return(0,program,i,1)

firstiter = 0
while True:
	if firstiter == 0:
		print('first iteration')
		(out,prog,step,haltstate) = opcode(myprog,0,2,0)
		print('output = ',out)
	else: (out,prog,step,haltstate) = opcode(prog,step,0,0)
	print('Output = ',out)
	if haltstate == 1:
		print('halted.')
		break
	else: continue
	


\
