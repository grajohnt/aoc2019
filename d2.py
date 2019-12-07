import csv

program = []

f = open("d2.txt")
for row in csv.reader(f):
	program = row

program = [int(i) for i in program]
print(program)
i = 0

while True:
	print(program[i])
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
	elif program[i] == 99:
		break


print(program)


