import sys
import re
#Dictionary for the FSA
FSA = {}
M = [] #List for the model
fsaouput = ''
for line in sys.stdin:
   fsaouput = fsaouput + line
   line = re.sub('(.*)\n', '\\1', line)
   m = re.search('([^ ]+) (.*)',line) 
   if m != None:
      if m.group(1)=='S':                
         if ('S' in FSA):
            FSA['S'].append(m.group(2))
         else :
            FSA['S'] = [m.group(2)]

      if m.group(1)=='F':
         if ('F' in FSA):
            FSA['F'].append(m.group(2))
         else :
            FSA['F'] = [m.group(2)] 

      if m.group(1)=='M':                
         T = re.split(' +',m.group(2))
         transtionList = [T[0], T[1], T[2]]
         M.append(transtionList)
      
FSA['M'] = M

#print FSA
#Reversing the FSA : 
temp = FSA['S']
FSA['S'] = FSA['F']
FSA['F'] = temp

for x in FSA.get('M'):
   temp = x[0]
   x[0] = x[2]
   x[2] = temp

print 'a)'
print fsaouput
f = open('fsarecmodel.txt', 'w')
print 'b)'
for x in FSA:
   if (x=='S'):
      for y in FSA.get('S'):
         str1 = 'S' + ' ' + y
         print str1
         f.write(str1 + '\n')

   if (x=='F'):
      for y in FSA.get('F'):
         str1 = 'F' + ' ' + y
         print str1
         f.write(str1 + '\n')

   if (x == 'M'):
      for y in FSA.get('M'):
         str1 = 'M' + ' ' + y[0] + ' ' + y[1] + ' ' + y[2] 
         print str1
         f.write(str1 + '\n')
f.close()