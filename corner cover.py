rawInput = """ """ # input
T = 200 # number of T

Tcases = [list(map(int, line.split())) for line in rawInput.splitlines()]
results = []

for case in Tcases:
    n = case[0]
    m = case[1]
    A = case[2]
    B = case[3]
    if (A==n and B<=m) or (B==m and A<=n) or (B==n and A<=m) or (A==m and B<=n):
        results.append("YES")
    else: results.append("NO")
    
if len(results)==200:
    output = '\n'.join(results)
    print(output)