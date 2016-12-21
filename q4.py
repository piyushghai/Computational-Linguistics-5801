import re
import sys
import model

R = model.Model('R')
W = model.Model('W')
O = model.CondModel('O')
ProbR = {}
probRSum = 0.0

def parseTrials(line):
        m = re.search('^ *'+'I' + ' *' + '(.*)', line)
        if m is not None:
        	s = m.group(1)
        	return re.split(' +', s)

for line in sys.stdin:
	R.read(line)
	W.read(line)
	O.read(line)
	I = parseTrials(line)

for r in R:
	ProbR[r] = R[r]
	for o in I:
		prob = 0.0
		for w in W:
			prob = prob + (O[r,w][o] * W[w])
		ProbR[r] = ProbR[r] * prob
	probRSum = probRSum + ProbR[r]

for r in R:
	ProbR[r] = ProbR[r] / probRSum
	print('RgivenIdata : ' + r + ' = ' + str(round(ProbR[r], 3)))



