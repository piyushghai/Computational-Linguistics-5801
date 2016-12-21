import sys
import re
#Initialize blank dictionaries
wordCount = {}
wordList = []
adjacentWordCount = {}
for line in sys.stdin:
  line = re.sub('(.*)\n', '\\1', line) #Substitute the new lines
  line = re.split(' ', line)  #Split on spaces
  for words in line:
    words = re.split('[\'\"?,.!:]', words) #Split on punctuations
    for word1 in words:
      if (word1 != ''):
        wordList.append(word1)
        if (word1 in wordCount):
          wordCount[word1] = wordCount[word1] + 1
        else:
          wordCount[word1] = 1

for i in range(0, len(wordList) - 1):
  if ((wordList[i], wordList[i+1]) in adjacentWordCount):
    adjacentWordCount[wordList[i], wordList[i+1]] = adjacentWordCount[wordList[i], wordList[i+1]] + 1

  else:
    adjacentWordCount[wordList[i], wordList[i+1]] = 1

# Print words
print '\na)'
for x in wordList:
  print x

print '\nb)'
#Print word Count
for x in wordCount:
  print x + ' ' + str(wordCount[x]) #Print all words with their counts

print '\nc)'
#Print adjacent words
for x in adjacentWordCount:
  print x[0] + ' ' + x[1] + ' ' + str(adjacentWordCount[x])


