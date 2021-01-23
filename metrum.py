 #metrum.pu

from collections import Counter, OrderedDict


with open('metrum.txt', 'r') as input_file:
    text = [t[:-1] for t in input_file.readlines()]
    print (len(text))


sonnetnumber = '0'
linenumber = 0
anapests = {x:0 for x in range(6)}
lines = []

for t in text:
    if t[0] == '-': 
        # if linenumber != 14: print (linenumber, sonnetnumber)
        linenumber = 0
        sonnetnumber = t
    else: 
        lines.append(t)
        linenumber +=1
        for number, foot in enumerate(t):
            if foot == 'A': anapests[number] += 1
            if foot == '\'' : anapests[number] += 1


print (anapests)
#print (lines)
print (OrderedDict(sorted(Counter(lines).items())))