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
    ang = (ang+360)%360
    return ang

def distance(A,B): 
    return m.sqrt(pow(B[0]-A[0],2)+pow(B[1]-A[1],2))

with open('d10.txt') as f:
 for l in f:
  for c in l:
   if c=='#':
    ast.append((i,j))
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

x = 11
y = 13
#ast.remove((y,x))
angles = []
distances = []

for a in range(len(ast)):
 if ast[a] != (11,13):
  angles.append(angle((11,13),ast[a]))
  distances.append(distance((11,13),ast[a]))
  
  
print(angles)
print(distances)
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