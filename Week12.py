#   PrintOutput
#   John Matocha
#   ​CSCI 102 – Section A
#   Week 12 - Part A
def PrintOutput(string):
    print('OUTPUT', string)

#   LoadFile
#   John Matocha
#   ​CSCI 102 – Section A
#   Week 12 - Part A
def LoadFile(file):
    lines = open(file, 'r').readlines()
    final = []
    for i in lines:
        list1 = i.split()
        for k in list1:
            final.append()
    return final

#   UpdatedString
#   John Matocha
#   ​CSCI 102 – Section A
#   Week 12 - Part A
def UpdateString(string1, string2, int1):
    newstring = ''
    
    for i in range(len(string1)):
        if i == int1:
            newstring+=string2
        else:
            newstring += string1[i]
         
            
    print(newstring)

#   ScoreFinder
#   John Matocha
#   ​CSCI 102 – Section A
#   Week 12 - Part A
def ScoreFinder(play, score, name):
    index = -1
    name = name.lower()
    print(name)
    for i in range(len(play)):
        play[i] = play[i].lower()
    for i in range(len(play)):
        if name == play[i]:
            index = i
    if index >= 0:
        print('OUTPUT', play[index], 'got a score of', score[index])
    else:
        print('OUTPUT player not found')

#   Union
#   John Matocha
#   ​CSCI 102 – Section A
#   Week 12 - Part A
def Union(list1, list2):
    newlist = []
    newlist = list(set(list1) | set(list2))
    return newlist
