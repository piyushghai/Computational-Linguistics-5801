import sys
import re
import model

P = model.Model('P')
R = model.CondModel('R')
T = model.CondModel('T')

ProbTGivenP = {}

for line in sys.stdin:
	P.read(line)
	R.read(line)
	T.read(line)

for p in P :
	for r in R[p] :
		for t in T[p,r] :
			ProbTGivenP[(p,t)] = ProbTGivenP.get((p,t), 0.0)  + (T[p,r][t] * P[p] * R[p][r])

for p,t in ProbTGivenP :
	ProbTGivenP[(p,t)] = ProbTGivenP.get((p,t), 0.0)/P[p]

for p,t in ProbTGivenP :
	print ('T ' + p + ' : ' + t + ' = ' + str(ProbTGivenP[(p,t)]))

	