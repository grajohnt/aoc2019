import numpy as np
import math as m

ast = []
locs = []
a = 0
i = 0
j = 0
debug=1


#def angle(p1, p2):
#    ang1 = np.arctan2(*p1[::-1])
#    ang2 = np.arctan2(*p2[::-1])
#    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

#def angle(p1, p2):
#    ang1 = np.arctan2(*p1[::-1])
#    ang2 = np.arctan2(*p2[::-1])
#    ang = np.rad2deg((ang1 - ang2) % (2 * np.pi))

def angle(A,B):
 ang = m.degrees(m.atan2(B[1]-A[1],B[0]-A[0]))
 ang = (90-ang)%360
 return(ang)
    

#def angle(A,B):
#    ang = m.degrees(m.atan2(B[1]-A[1],B[0]-A[0]))
#    ang = m.degrees(m.atan2(B[0]-A[0],B[1]-A[1])-m.pi/2)
#    ang = (ang+360)%360
#    return ang

#def angle(vector1, vector2):
#    x1, y1 = vector1
#    x2, y2 = vector2
#    dot = x1*x2 + y1*y2
#    det = x1*y2 - y1*x2
#    angle = m.atan2(det, dot)
#    return (2*m.pi + angle) if angle < 0 else angle

#from math import degrees, atan2
#def angle(x, y):
# center_x = 0
# center_y = 0
# angle = degrees(atan2(y - center_y, x - center_x))
# bearing1 = (angle + 360) % 360
# bearing2 = (90 - angle) % 360
# #print "gb: x=%2d y=%2d angle=%6.1f bearing1=%5.1f bearing2=%5.1f" % (x, y, angle, bearing1, bearing2)
# return


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
  #print('ang between ',x,',',-y,' and',ast[a][0],-ast[a][1],'is ',angle((x,-y),(ast[a][0],-ast[a][1])))
  distances.append(distance((x,y),ast[a]))
  
count = 0

cir = 360
mult = 10

while count < 200:
 #for ang in range(0,360):
 for ang in range(0,cir*mult):
  #if ang == 360: ang = 0
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
