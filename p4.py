import re
import sys

# a Tree consists of a category label 'c' and a list of child Trees 'ch'
class Tree:
    
    def __init__ (this):
        this.count = 0
    # Keep count of nodes in the tree
    def getCount(this):
        return this.count

    def read(this,s):
        this.ch = []
        # a tree can be just a terminal symbol (a leaf)
        m = re.search('^ *([^ ()]+) *(.*)',s)
        if m != None:
            this.c = m.group(1)
            this.count = 1 #Increment counter here
            return m.group(2)

        # a tree can be an open paren, nonterminal symbol, subtrees, close paren
        m = re.search('^ *\( *([^ ()]*) *(.*)',s)
        if m != None:
            this.c = m.group(1)
            s = m.group(2)
            this.count = 1 #Increment counter here
            m = re.search('^ *\)',s)
            while re.search('^ *\)',s) == None:
                t = Tree()
                s = t.read(s)
                this.ch = this.ch + [t]
                this.count = this.count + t.getCount() #Increment counter for the parent tree by adding children's nodes
            x = re.search('^ *\) *(.*)',s).group(1)
            return x
        return ''

# for each line in input
for line in sys.stdin:
      # for each tree in line
    if line != '':
            t=Tree()
            line = t.read(line)
            print t.getCount() #print the result