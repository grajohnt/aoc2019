import csv
import copy

program = []

f = open("d2.txt")
for row in csv.reader(f):
	program = row

program = [int(i) for i in program]

orig_program = copy.copy(program)
i = 0
for noun in range(1,99):
	print("Noun: ",noun)
	for verb in range(1,99):
		print("Verb: ",verb)
		program[1] = noun
		program[2] = verb
		print(program)
		while program[i] != 99:
			if program[i] == 1:
				in1 = program[i+1]
				in2 = program[i+2]
				out = program[i+3]
				program[out] = program[in1]+program[in2] 
				i = i+4
				print(i)
			elif program[i] == 2:
				in1 = program[i+1]
				in2 = program[i+2]
				out = program[i+3]
				program[out] = program[in1]*program[in2]
				i = i+4
		print("END")
		if program[0] == 19690720:
			cnoun = copy.copy(noun)
			cverb = copy.copy(verb)
			print("HIT!!")
			print("NOUN: ",cnoun)
			print("VERB: ",cverb)
		program = copy.copy(orig_program)
		print(program)
		i=0	
		

print("Correct Noun = ",cnoun)
print("Correct Verb = ",cverb)


