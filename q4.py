import re
import sys
import model

PiY = model.Model('Y')
ThetaX = model.CondModel('XgivY')
ThetaY = model.CondModel('YgivY')
yPrev = {}

def parseInput(line):
        m = re.search('^ *'+'I' + ' *' + '(.*)', line)
        if m is not None:
        	s = m.group(1)
        	return re.split(' +', s)

## All models read in
for line in sys.stdin:
	PiY.read(line)
	ThetaX.read(line)
	ThetaY.read(line)
	I = parseInput(line)

for y in PiY:
	yPrev[y] = PiY[y] * ThetaX[y][I[0]]

#For next part loop over all y i.e result in second question
for t in range(1,len(I)):
	yNext={}
	for y0 in ThetaY:
		for y1 in ThetaY[y0]:
			yNext[y1] = yNext.get(y1,0.0) + (yPrev.get(y0, 0.0) * ThetaY[y0][y1] * ThetaX[y1][I[t]])
	yPrev = yNext

for y in yNext:	
	print 'Y_fwd : ' + y + ' = ' + str(yNext[y])
