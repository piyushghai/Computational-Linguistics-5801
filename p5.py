import re
import sys

# a Tree consists of a category label 'c' and a list of child Trees 'ch'
class Tree:
    
    def __init__ (this):
        this.count = 0
        this.terminalSymbols = [] #Keep track of all terminal symbols
    # obtain tree from string
    def getCount(this):
        return this.count

    def getTerminalSymbols(this):
        return this.terminalSymbols #Return the list of all terminals

    def read(this,s):
        this.ch = []
        # a tree can be just a terminal symbol (a leaf)
        m = re.search('^ *([^ ()]+) *(.*)',s)
        if m != None:
            this.c = m.group(1)
            this.count = 1
            this.terminalSymbols = this.terminalSymbols + [m.group(1)] #Found a terminal here
            return m.group(2)

        # a tree can be an open paren, nonterminal symbol, subtrees, close paren
        m = re.search('^ *\( *([^ ()]*) *(.*)',s)
        if m != None:
            this.c = m.group(1)
            s = m.group(2)
            this.count = 1
            m = re.search('^ *\)',s)
            while re.search('^ *\)',s) == None:
                t = Tree()
                s = t.read(s)
                this.ch = this.ch + [t]
                this.terminalSymbols = this.terminalSymbols + t.getTerminalSymbols() #Append children's terminals to parent node
            x = re.search('^ *\) *(.*)',s).group(1)
            return x
        return ''

num = -1
# for each line in input
for line in sys.stdin:
      # for each tree in line
    if line != '':
        if num == -1: #Read the number from the first line
            num = line.strip()
        else :    
            t=Tree()
            line = t.read(line)
            print t.getTerminalSymbols()[int(num)-1] #Print the nth terminal symbol