rawInput = """
"""

rawInputList = rawInput.splitlines()
T = int(rawInputList[0])
Tresults = []
for i in range(1, len(rawInputList), 2):
    n = int(rawInputList[i])
    orbsRaw = rawInputList[i+1]
    orbsPower = list(map(int, orbsRaw.split()))
    
    sortPower = orbsPower.copy()
    sortPower.sort(reverse = True)  # to sort descending
    
    for i in range(len(sortPower)-1):
        y = sortPower[0]
        x = sortPower[1]
        newOrb = x + 2*y
        sortPower.pop(0)
        sortPower.insert(0, newOrb)
        sortPower.pop(1)
    
    Tresults.append(str(sortPower[0] % (10**9 + 7)))
    
if len(Tresults) == T:
    output = '\n'.join(Tresults)
    print(output)



