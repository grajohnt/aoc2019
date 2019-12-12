import numpy as np
import math as m

ast = []
locs = []
a = 0
i = 0
j = 0
debug=1

def angle(A,B):
 ang = m.degrees(m.atan2(B[1]-A[1],B[0]-A[0]))
 ang = (90-ang)%360
 return(ang)

def distance(A,B): 
    return m.sqrt(pow(B[0]-A[0],2)+pow(B[1]-A[1],2))

with open('d10.txt') as f:
 for l in f:
  #print(l)
  for c in l:
   if c=='#':
    ast.append((j,i))
   elif c=='.':
    next
   else: break
   #if debug==1: print('i=',i,' j=',j,' c=',c)
   #ast[i,j] = a   
   j = j+1
  k = j
  j = 0
  i = i+1

print('i=',i,' j=',j)
totals=np.zeros((i,k))

#for a in range(len(ast)):
# totals[ast[a]] = 1
#print(ast)
#totals[ast] = 1 
#print(totals)

# Need to compute distance, then rotate through angles 

x = 13 
y = 11 
#ast.remove((y,x))
angles = []
distances = []

for a in range(len(ast)):
 if ast[a] != (x,y):
  angles.append(angle((x,-y),(ast[a][0],-ast[a][1])))
  print('ang between ',x,',',-y,' and',ast[a][0],-ast[a][1],'is ',angle((x,-y),(ast[a][0],-ast[a][1])))
  distances.append(distance((x,y),ast[a]))
  
count = 0

cir = 360
mult = 10

while len(ast) > 0:
 #for ang in range(0,360):
 for ang in range(0,cir*mult):
  if ang == 360: ang = 0
  ang = ang/mult 
  ids = [i for i in range(len(angles)) if angles[i] >= ang and angles[i] < ang+(1/mult)] 
  if len(ids) > 0:
   dist = 100
   for idx in ids:
    print('dist = ',distances[idx],'ang = ',angles[idx])
    if distances[idx] < dist: 
     minidx = idx
     dist = distances[idx]
   print('blowing up at coords',ast[minidx],' with angle ',angles[minidx],' and distance',distances[minidx])
   angles.pop(minidx)
   distances.pop(minidx)
   ast.pop(minidx)
   count = count+1
   print(count)
  
  
#print(angles)
#print(distances)
#for a in range(len(ast)):
# if 

#for p in range(len(ast)):
# angles = []
# for a in range(len(ast)):
#  if p!=a:
#   angles.append(angle(ast[p],ast[a]))
# print(len(set(angles)))
# print('p=',p)
# totals[ast[p]] = len(set(angles))
 
#print(totals)
#print(totals.max())
#print('x=',np.where(totals == totals.max())[1],' y=',np.where(totals == totals.max())[0])
