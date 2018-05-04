coins = 1, 5, 10, 25, 21
target = 10
states = {s:0 for s in range(1,target+1)}

def change(v, states):
    if len(states) < v:
        print("extending states arrary to ", v)
        states = {s:0 for s in range(1,v+1)}
    if v < 1:
        return 0
    elif states[v] != 0:
        return states[v]
    elif v in coins:
        states[v] = 1
    else:
        acoins = list(filter(lambda c : c < v, coins))
        results = []
        for c in acoins:
            results.append(change(v-c, states)+1)
        states[v] = min(results)
    return states[v]   

change(128, states)
