#   YOUR GITHUB REPO
# Joseph Hall
# ​CSCI 102 – Section B
# Week 11 - Part B



import string

players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
x = 0
count = 0
newf = []
inter = []
##########################
def PrintOutput(astring):
    print('OUTPUT', astring)
##########################
def LoadFile(file):
    with open(file, "r") as f:
        for line in f:
            newf.append(line)
        return newf
##########################
def UpdateString(s1,s2,index):
    new = s1[:index] + s2 + s1[index+1:]
    return new
##########################
def FindWordCount(l, s):
    global x
    global count
    while 0 < len(s):
        x = s.find(l, x)
        if x == -1:
            break
        count += 1
        x += 1
    return count
##########################
def ScoreFinder(players, scores, name):
    x = players.index(name) 
    if name in players:
        print('OUPUT', name, 'got a score of', scores[x])
##########################
def Union(l1, l2):
    union = l1 + l2
    print("OUTPUT", union)
##########################
def Intersection(l1, l2):
    for c in l1:
        if c in l2:
            inter.append(c)
    print("OUTPUT", inter)
            

    
