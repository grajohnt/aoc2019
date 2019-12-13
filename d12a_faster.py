import re
import numpy as np

debug = 1

def gcd(x,y):
 while(y):
  x,y=y,x%y
 return x

def lcm(x,y):
 return (x*y)//gcd(x,y)

p = [[[] for i in range(1)] for i in range(4)]
v = [[[0] for i in range(1)] for i in range(4)]

pattern = re.compile('(?:=)(-?\d+)')
for i, line in enumerate(open('d12.txt')):
 match = re.findall(pattern,line)
 #x[i] = np.array([int(match[0]),int(match[1]),int(match[2])])
 p[i][0] = int(match[0])
 #p[i][1] = int(match[1])
 #p[i][2] = int(match[2])
 
pos = np.array(p)
vel = np.zeros(pos.shape)

#pot = np.zeros(4)  
#kin = np.zeros(4) 
#total = np.zeros(4) 

tmp = np.concatenate((pos,vel),axis=1) 
hist = np.array([]) 
orig = np.append(hist,tmp.flatten())
print(orig)

#if debug==1: print(pos)

ans=[]

n = 1000000 

for i in range(3):

 for j, line in enumerate(open('d12.txt')):
  match = re.findall(pattern,line)
  p[j][0] = int(match[i])
 pos = np.array(p)
 vel = np.zeros(pos.shape)
 tmp = np.concatenate((pos,vel),axis=1)
 hist = np.array([])
 orig = np.append(hist,tmp.flatten())

 for t in range(n):
  for moon in range(4):
   vel[moon,0] = vel[moon,0] + len(np.where(pos[:,0] > pos[moon,0])[0]) - len(np.where(pos[:,0] < pos[moon,0])[0])
  for moon in range(4):
   pos[moon,0] = pos[moon,0] + vel[moon,0]
  tmp = np.concatenate((pos,vel),axis=1) 
  tmp = tmp.flatten()
  if t>0:
   if np.array_equal(tmp,orig):
    print('Found match for ',i,' at t =',t+1)
    ans.append(t+1)
    break

print(lcm(lcm(ans[0],ans[1]),ans[2]))
