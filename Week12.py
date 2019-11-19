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
