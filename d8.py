import numpy as np
from PIL import Image

im = []

w = 25 
h = 6 

with open('d8.txt') as f:
 for line in f:
  ln = line.strip()
  for c in str(ln):
   im.append(int(c))

l = len(im)/w/h 
l = int(l)
print('Layers = ',l)

#image = np.reshape(im,(h,l,w))
image = np.reshape(im,(l,h,w))
#print(image.shape)
#print(image[2,:,:])
# Ugh - that's layer, row, column - I hate numpy

minl0 = 9999

for k in range(l):
 print('Layer = ',k)
 print('Zero digits = ',np.sum(image[k,:,:]==0))
 l0 = np.sum(image[k,:,:]==0)
 print('One digits = ',np.sum(image[k,:,:]==1))  
 l1 = np.sum(image[k,:,:]==1)
 print('Two digits = ',np.sum(image[k,:,:]==2))
 l2 = np.sum(image[k,:,:]==2)
 if l0 < minl0:
  minl0 = l0
  print('Multiplied value is: ',l1*l2)




