from PIL import Image, ImageDraw 

dim = 12000 

img = Image.new('RGB',(dim,dim), color = 'black')
#pixels = img.load()
draw = ImageDraw.Draw(img)

path = []

centerx = dim/2-2000
centery = dim/2+2000

draw.ellipse((centerx-10,centery-10,centerx+10,centery+10),fill='white',outline=None)
colors = ['red','blue']
k = 0

with open('d3.txt') as f:
	for line in f:
		i = centerx 
		j = centery 
		tsteps = 0
		path = [x.strip() for x in line.split(',')] 
		c = colors[k]	
		for l in path:
			dir = l[0]
			steps = int(l[1:])
			tsteps = tsteps+steps
			if dir == "R":
				draw.line((i,j,i+steps,j),fill=c)
				#pixels[i,j:j+steps] = 1
				i = i+steps
				draw.text((i-50,j-50),str(tsteps),fill='white',outline='white')
			elif dir == "L":
				draw.line((i,j,i-steps,j),fill=c)
				#pixels[i,j:j-steps] = 1
				i = i-steps
				draw.text((i-50,j-50),str(tsteps),fill='white',outline='white')
			elif dir == "U":
				draw.line((i,j,i,j-steps),fill=c)
				#pixels[i:i+steps,j] = 1
				j = j-steps
				draw.text((i-50,j-50),str(tsteps),fill='white',outline='white')
			elif dir == "D":
				draw.line((i,j,i,j+steps),fill=c)
				#pixels[i:i-steps,j] = 1
				j = j+steps
				draw.text((i-50,j-50),str(tsteps),fill='white',outline='white')
		k = k+1


img.save('wiring.png')
#img.show()

