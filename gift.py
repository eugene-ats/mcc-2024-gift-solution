rawInput = """<task input>"""
guestsTier = list(map(int, rawInput.split()))

numOfGuests_n = 1000
numOfGifts_m = 746
sortedTier = list(guestsTier)   # a separate list in asc order
sortedTier.sort()

results = [str(nil-nil) for nil in range(numOfGuests_n)] # initial list with all guest getting 0

guestReceive = sortedTier[0:numOfGifts_m]  # the list that contains only the first m guest with highest tier

for x in range(len(guestsTier)):     # loop over each guest
    if guestsTier[x] in guestReceive:   # if the guest's tier is in the receiving list
        results[x] = "1"                # change its corresponding bin code to '1'
        guestReceive.remove(guestsTier[x])   # in the end the receiving list will be empty
        

# double checking
n = 0
for y in results:
    if y=="1":
        n+=1
        
if n==numOfGifts_m:
    print()
    print(' '.join(results))
