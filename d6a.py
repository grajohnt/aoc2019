from anytree import Node, RenderTree, Walker

orbits = {}

with open('d6.txt') as f:
    for l in f:
        db = 0
        orb = l.strip().split(")")
        if orb[0] == 'SAN' or orb[1] == 'SAN':
            #print(l)
            db = 0
        if orb[0] in orbits:
            if orb[1] in orbits:
                orbits[orb[1]].parent = orbits[orb[0]]
                if db==1: print('Attached existing ', orb[1], ' to parent ', orb[0])
                #orbits[orb[1]] = Node(orb[1], parent=orbits[orb[0]])
            else:
                orbits[orb[1]] = Node(orb[1], parent=orbits[orb[0]])
                if db==1: print('Attached new ', orb[1], ' to parent ', orb[0])
        else:
            orbits[orb[0]] = Node(orb[0])
            if db==1: print('Added new parent node ',orb[0])
            if orb[1] in orbits:
                orbits[orb[1]].parent = orbits[orb[0]]
                if db==1: print('Attached ',orb[0],' to parent ', orb[1])
            else:
                orbits[orb[1]] = Node(orb[1], parent=orbits[orb[0]])
                if db==1: print('Added new child node ',orb[1])


#print(orbits[orb[1]].ancestors)
#print(orbits[100].ancestors)
#a = 'X31'
a = 'YOU'
b = 'SAN'

w = Walker()
(u,com,d) = w.walk(orbits[a],orbits[b])
steps = (len(u)-1)+(len(d)-1)
print('Steps = ',steps)

print('up = ',len(u),', down = ',len(d),', common = ',com)
#for pre, fill, node in RenderTree(orbits[com]): print("%s%s" % (pre, node.name))


#for p in path:
#    print(p)
#rint(orbits[a].ancestors)
#for pre, fill, node in RenderTree(orbits[a].ancestors[0]): print("%s%s" % (pre, node.name))
#for pre, fill, node in RenderTree(orbits[a]): print("%s%s" % (pre, node.name))

#for pre, fill, node in RenderTree(orbits[8B3]): print("%s%s" % (pre, node.name))
#print(orbits)
total = 0
for o in orbits:
    #print(orbits[o], ' length = ',orbits[o].depth)
    total = total + orbits[o].depth
print(total)