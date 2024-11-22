rawInput = '''<raw task input>'''

rawList = rawInput.splitlines()
line1 = list(map(int, rawList[0].split()))
n_numOfTarget = line1[0]
m_multiplier = line1[1]
K_numOfArrows = line1[2]
targetHP = list(map(int, rawList[1].split()))

# print('no. of arrows: ', K_numOfArrows)
# print(targetHP)

def find_newHP(j, i, M, X, hp):
    damage = max(0, M*X - (j-i)**2)
    #print(f'damage to target {j}: {M}*{X} - ({j}-{i})**2 = {hp} - {damage} = {hp-damage}')
    return hp-damage
    
def tryShoot(X, K_numOfArrows, i, n_numOfTarget, m_multiplier, trialList):
    # trial = trialList
    k=0
    while k < K_numOfArrows:   # for each arrow
        # print('shooting', k+1, 'arrow')
        startingPos = i  # startingPos = index of first target alive
        # print('startingPos:', startingPos)
        if startingPos>=n_numOfTarget:
            print('startingPos exceeds range (', startingPos, ')')
            break
        for j in range(startingPos, n_numOfTarget):
            newHP = find_newHP(j, startingPos, m_multiplier, X, trialList[j])
            trialList[j] = newHP
        i = next((index for index, el in enumerate(trialList) if el > 0), 0)
        k += 1
    return k

foundX = False
X = 10000
stepping = 1000

while foundX != True:
    i = 0   # indices of initial first target i
    trial = targetHP.copy()  # resets the HP of targets on every power
    print('shooting with power', X)
    k = tryShoot(X, K_numOfArrows, i, n_numOfTarget, m_multiplier, trial)
    print('no. of arrows used', k)
    print(trial)
  
      
    if all(v <= 0 for v in trial) and k==K_numOfArrows:
        # print(trial)
        isMin = False
        reverseI = 1
        while isMin != True:
            trial2 = targetHP.copy()
            print('testing for power X=', X-reverseI)
            k = tryShoot(X-reverseI, K_numOfArrows, i, n_numOfTarget, m_multiplier, trial2)
            if all(v2 <= 0 for v2 in trial2) and k==K_numOfArrows:
                reverseI += 1
            else:
                isMin = True
        foundX = True
        print('minimum value of X = ', X-reverseI+1)
    elif all(v <= 0 for v in trial) and k<K_numOfArrows:
        print('num of arrow shot (',k, ') is less than', K_numOfArrows)
        X-= stepping
    else: 
        X += stepping

