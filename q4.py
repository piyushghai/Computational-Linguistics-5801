import sys
import re
import model

A = model.Model('A')
B = model.CondModel('B')
PB = {}

for line in sys.stdin:
	A.read(line)
	B.read(line)

for a in A :
	for b in B[a] :
		PB[b] = PB.get(b, 0.0) + (A[a] * B[a][b])

for b in PB :
	print('B : ' +b+ ' = ' + str(PB[b]))