import re
import numpy as np

debug = 1


p = [[[] for i in range(3)] for i in range(4)]
v = [[[0] for i in range(3)] for i in range(4)]

pattern = re.compile('(?:=)(-?\d+)')
for i, line in enumerate(open('d12.txt')):
 match = re.findall(pattern,line)
 #x[i] = np.array([int(match[0]),int(match[1]),int(match[2])])
 p[i][0] = int(match[0])
 p[i][1] = int(match[1])
 p[i][2] = int(match[2])
 
pos = np.array(p)
vel = np.array(v)

print(pos.max(axis=0)[0])

pot = np.zeros(4)  
kin = np.zeros(4) 
total = np.zeros(4) 


if debug==1: print(pos)

n = 1000

for t in range(n):
 for moon in range(4):
  # x coords < current
  vel[moon,0] = vel[moon,0] + len(np.where(pos[:,0] > pos[moon,0])[0]) - len(np.where(pos[:,0] < pos[moon,0])[0])
  vel[moon,1] = vel[moon,1] + len(np.where(pos[:,1] > pos[moon,1])[0]) - len(np.where(pos[:,1] < pos[moon,1])[0])
  vel[moon,2] = vel[moon,2] + len(np.where(pos[:,2] > pos[moon,2])[0]) - len(np.where(pos[:,2] < pos[moon,2])[0])
 for moon in range(4):
  pos[moon,0] = pos[moon,0] + vel[moon,0]
  pos[moon,1] = pos[moon,1] + vel[moon,1]
  pos[moon,2] = pos[moon,2] + vel[moon,2]
  pot[moon] = abs(pos[moon,0])+abs(pos[moon,1])+abs(pos[moon,2])
  kin[moon] = abs(vel[moon,0])+abs(vel[moon,1])+abs(vel[moon,2])
  total[moon] = pot[moon] * kin[moon]
  #print('pot = ',pot[moon],' kin = ',kin[moon],' total = ',total[moon]) 
  
print('Total after ',n,' steps = ',total.sum())
  
