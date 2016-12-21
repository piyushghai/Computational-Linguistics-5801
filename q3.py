import re
import sys
import model

G = model.Model('G')
P = model.CondModel('P')
C = model.CondModel('C')

ProbCGivenP = {}
ProbPGivenG = {}
ProbPCommaG = {} 
ProbP = {}
ProbCCommaP = {}
ProbC = {}
ProbPGivenC = {}

for line in sys.stdin:
	G.read(line)
	P.read(line)
	C.read(line)

for g in G :
	for p in P[g]:
		ProbPGivenG[(p,g)] = P[g][p]
		for c in C[p]:
			ProbCGivenP[(c,p)] = C[p][c]
		
for (p,g) in ProbCGivenP:
	ProbPCommaG[(p,g)] = ProbPGivenG[(p,g)] * G[g]

for (p,g) in ProbPCommaG:
	ProbP[p] = ProbP.get(p,0.0) + ProbPCommaG[(p,g)]

for (c,p) in ProbCGivenP:
	ProbCCommaP[(c,p)] = ProbCGivenP[(c,p)] * ProbP[p]

for (c,p) in ProbCCommaP:
	ProbC[c] = ProbC.get(c,0.0) + ProbCCommaP[(c,p)]

for (c,p) in ProbCCommaP:
	ProbPGivenC[(p,c)] = ProbCCommaP[(c,p)]/ProbC[c]

for (p,c) in ProbPGivenC:
	print("PgivC " + c + " : " + p + " = " + str(ProbPGivenC[(p,c)]))









