import re
import sys

preTermMap = {}
count = 0
class Tree:

    def read(this,s):
    	global count
        this.ch = []
        # a tree can be just a terminal symbol (a leaf)
        m = re.search('^ *([^ ()]+) *(.*)',s)
        # Extracting a complete leaf subtree of the form : (V-aN-bN has boy)
        m2 = re.search('^\(( *[^()]*)\) *(.*)',s)

        if m2!= None:
            s2 = m2.group(1)
            s3 = re.split('\s+', s2)
            if len(s3) > 1:
                nonTerminal = s3[0]
                #Found Latest PreTerminal symbol
                count = count + 1
                if count == 1:
                    preTermMap[nonTerminal] = preTermMap.get(nonTerminal, 0.0) + 1

        if m != None:
            return m.group(2)

        # a tree can be an open paren, nonterminal symbol, subtrees, close paren
        m = re.search('^ *\( *([^ ()]*) *(.*)',s)
        if m != None:
            s = m.group(2)
            this.count = 1
            m = re.search('^ *\)',s)
            while re.search('^ *\)',s) == None:
                t = Tree()
                s = t.read(s)
                this.ch = this.ch + [t]
            x = re.search('^ *\) *(.*)',s).group(1)
            return x
        return ''

# for each line in input
for line in sys.stdin:
	count = 0
	t = Tree()
	t.read(line)

sum = 0
for x in preTermMap:
    sum = sum + preTermMap[x]

for x in preTermMap:
    print ('Y' + ' : ' + x + ' = ' + str(round((preTermMap[x]/sum), 8)))
    