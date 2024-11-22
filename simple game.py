rawInput = '''
'''
rawList = rawInput.splitlines()
noOfPairs = int(rawList[0])
rawList.pop(0)

pairs = [list(map(int, line.split())) for line in rawList]
n = len(pairs)
print(pairs)

Xscore = 0
Yscore = 0

def index_of_largest(arr):
    return max(range(len(arr)), key=arr.__getitem__)

def chooseX():
    choicesX = []
    for pair in pairs:
        choicesX.append(pair[0])
    i = index_of_largest(choicesX)
    global Xscore
    Xscore += choicesX[i]
    print(pairs[i])
    pairs.pop(i)
    
def chooseY():
    choicesY = []
    for pair in pairs:
        choicesY.append(pair[1])
    i = index_of_largest(choicesY)
    global Yscore
    Yscore += choicesY[i]
    print(pairs[i])
    pairs.pop(i)

while n>0:
    chooseX()
    print('X: ', Xscore)
    n -= 1
    if n>0:
        chooseY()
        print('Y: ', Yscore)
        n -= 1
        
print()
print('X: ', Xscore)
print('Y: ', Yscore)
print('X - Y = ', Xscore-Yscore)



