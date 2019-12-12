import re

debug = 1

pos = [[[] for i in range(3)] for i in range(4)]
vel = [[[0] for i in range(3)] for i in range(4)]

pattern = re.compile('(?:=)(-?\d+)')
for i, line in enumerate(open('d12.txt')):
 match = re.findall(pattern,line)
 pos[i][0] = int(match[0])
 pos[i][1] = int(match[1])
 pos[i][2] = int(match[2])

if debug==1: print(pos)
for t in range(9):
 for p in range(4):
  #print('p=',p)
  vel[p][0] = pos[p][0]
  vel[p][1] = pos[p][1]
  vel[p][2] = pos[p][2]
  #print('p=',p)
  
print(vel)