# import standard input and regular expression modules
import sys
import re

# initialize FSA parameters as dictionaries
Q = {}
S = {}
F = {}
M = {}
Input = []

# for each line of input in model file
for line in sys.stdin:
   m = re.search('([^ ]+) (.*)',line) # identify FSA param and value
   if m != None:
      if m.group(1)=='S':                # if start state, add to S
         S[m.group(2)] = True
      if m.group(1)=='F':                # if final state, add to F
         F[m.group(2)] = True
      if m.group(1)=='M':                # if trans model tuple, add to M
         T = re.split(' +',m.group(2))     # isolate tuple elements
         M[T[0],T[1],T[2]] = True          # update M
         Q[T[0]] = True                    # update Q
         Q[T[2]] = True
      if m.group(1)=='I':                # if input, set as Input (starting at t=1)
         Input = ['-'] + re.split(' +',m.group(2))

# initialize table of possible states at time step 0 using start states
V = {}
for q in Q:
   V[0,q] = S.get(q,False)

# for each possible state qP in V at time t-1, for each qP,x,q in M, add q
for t in range(1,len(Input)):
   for qP in Q:
      for q in Q:
         V[t,q] = V.get((t,q),False) or (V[t-1,qP] and M.get((qP,Input[t],q),False))

# if any final states possible at end, accept
for q in F:
   if V[len(Input)-1,q] and F[q]:
      print ( 'yes' )
