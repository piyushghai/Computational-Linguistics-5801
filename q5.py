import re
import sys
import model

PiY = model.Model('Y')
ThetaX = model.CondModel('XgivY')
ThetaY = model.CondModel('YgivY')
yPrev = {}
prevSequenceForEveryY = {}

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

for y in ThetaY:
	yPrev[y] = PiY[y] * ThetaX[y][I[0]]
	prevSequenceForEveryY[y] = [y]

for t in range(1,len(I)):
	yNext={}
	currsequenceForEveryY = {}
	for y0 in ThetaY:
		for y1 in ThetaY[y0]:
			val = yNext.get(y1, 0.0)
			val2 = (yPrev.get(y0, 0.0) * ThetaY[y0][y1] * ThetaX[y1][I[t]])
			if val2 > val:
				yNext[y1] = val2
				currsequenceForEveryY[y1] = []
				currsequenceForEveryY[y1].extend(prevSequenceForEveryY[y0])
				currsequenceForEveryY[y1].append(y1)

	yPrev = yNext
	prevSequenceForEveryY = currsequenceForEveryY

## Alternative 1 Print just a single output 
max = 0.0
maxY = '###'
for y in yNext:
	if max < yNext[y]:
		max = yNext[y]
		maxY = y

## Found a maximal sequence output for y as output
if maxY != '###':
	mls = currsequenceForEveryY[maxY]

i=0
for y in mls:
	print 'preterminal ' + str(i+1) + ' = ' + y
	i = i+1