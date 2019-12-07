total = 0

for n in range (145852,616942):
 #print(n)
 count = {}
 sn = str(n)
 dead = 0
 ld = 0
 for d in sn: 
  if int(d) < ld:
   dead = 1
  else:
   ld = int(d)
  if d in count:
    count[d] += 1
  else:
    count[d] = 1
 for key in count:
  if count[key] > 1 and not dead:
   print(n)
   print(key, count[key])
   total = total+1
   #print(total)
   break 

print(total) 
