import re
import sys

# a Tree consists of a category label 'c' and a list of child Trees 'ch'
preTermpreTermMap = {}
preTermMap = {}
preTermGlobal = ''
class Tree:

    def read(this,s):
    	global preTermGlobal
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
                if preTermGlobal != '':
                    preTermMap[preTermGlobal] = preTermMap.get(preTermGlobal, 0.0) + 1
                    preTermpreTermMap[preTermGlobal, nonTerminal] = preTermpreTermMap.get((preTermGlobal, nonTerminal), 0.0) + 1
                    preTermGlobal = nonTerminal

                else : 
                    preTermGlobal = nonTerminal

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
	preTermGlobal = ''
	t = Tree()
	t.read(line)

for x,y in preTermpreTermMap:
    print ('YgivY ' + x + ' : ' + y + ' = ' + str(round(preTermpreTermMap[x,y]/preTermMap[x], 8)))
