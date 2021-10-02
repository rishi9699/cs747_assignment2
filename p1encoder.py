import numpy as np
f = open('./pa2_base/pa2_base/data/attt/states/states_file_p1.txt')
states = f.read().split()
states = dict(zip(states, range(len(states))))
states

f = open('./pa2_base/pa2_base/data/attt/policies/p2_policy2.txt')
sp = f.readline()
tmp = f.readline()

oppo_acts = {}
while tmp!='':
    oppo_acts[tmp.split()[0]] = list(np.array(tmp.split()[1:], dtype='float'))
    tmp = f.readline()
    
# big change for p1 code
print('numStates 2425')
print('numActions 9')
print('end 2423 2424')

for s in states:
    tmp = list(s)
    j=0
    while j<9:
        if tmp[j]=='0':
            tmp[j] = '1'
            if ''.join(tmp) in oppo_acts:
                probs = oppo_acts[''.join(tmp)]
                k=0
                while k<9:
                    if probs[k]!=0:
                        tmp[k]='2'
                        if ''.join(tmp) in states:
                            #go to tmp state
                            #print(s, ''.join(tmp))
                            print('transition', states[s], j, states[''.join(tmp)], str(0), probs[k])
                            #print()
                        else:
                            # go to win state
                            #print('player 2 ended the game, player 1 won', s, ''.join(tmp))
                            print('transition', states[s], j, '2424 1', probs[k])
                            #print()
                        tmp[k]='0'
                    k+=1
            else:
                # go to draw or lose state and reward 0
                #print(s,'player 1 did something foolish, player 2 won or draw', ''.join(tmp))
                print('transition', states[s], j, '2423 -1 1.0')
                #print()
            tmp[j]='0'
        j+=1
        
print('mdptype episodic')
print('discount  1.0')
