import numpy as np
f = open('./pa2_base/pa2_base/data/attt/states/states_file_p2.txt')
states = f.read().split()
states = dict(zip(states, range(len(states))))
states

f = open('./pa2_base/pa2_base/data/attt/policies/p1_policy2.txt')
sp = f.readline()
tmp = f.readline()

oppo_acts = {}
while tmp!='':
    oppo_acts[tmp.split()[0]] = list(np.array(tmp.split()[1:], dtype='float'))
    tmp = f.readline()
    
# big change for p1 code
print('numStates 2099')
print('numActions 9')
print('end 2097 2098')

def check1pattern(tmp):
    if tmp[0]=='1' and tmp[1]=='1' and tmp[2]=='1':
        return True
    elif tmp[3]=='1' and tmp[4]=='1' and tmp[5]=='1':
        return True
    elif tmp[6]=='1' and tmp[7]=='1' and tmp[8]=='1':
        return True
    elif tmp[0]=='1' and tmp[3]=='1' and tmp[6]=='1':
        return True
    elif tmp[1]=='1' and tmp[4]=='1' and tmp[7]=='1':
        return True
    elif tmp[2]=='1' and tmp[5]=='1' and tmp[8]=='1':
        return True
    elif tmp[0]=='1' and tmp[4]=='1' and tmp[8]=='1':
        return True
    elif tmp[2]=='1' and tmp[4]=='1' and tmp[6]=='1':
        return True
    else:
        return False
        

for s in states:
    tmp = list(s)
    j=0
    while j<9:
        if tmp[j]=='0':
            tmp[j] = '2'
            if ''.join(tmp) in oppo_acts:
                probs = oppo_acts[''.join(tmp)]
                k=0
                while k<9:
                    if probs[k]!=0:
                        tmp[k]='1'
                        if ''.join(tmp) in states:
                            #go to tmp state
                            #print(s, ''.join(tmp))
                            print('transition', states[s], j, states[''.join(tmp)], str(0), probs[k])
                            #print()
                        else:
                            # go to win state
                            #print('player 1 ended the game, player 2 won or draw', s, ''.join(tmp))
                            if '0' in tmp:
                                print('transition', states[s], j, '2098 1', probs[k]) #won
                            else:
                                if check1pattern(tmp):
                                    print('transition', states[s], j, '2098 1', probs[k]) #won
                                else:
                                    print('transition', states[s], j, '2097 -1', probs[k]) #draw
                            #print()
                        tmp[k]='0'
                    k+=1
            else:
                # go to draw or lose state and reward 0
                #print(s,'player 2 did something foolish, player 1 won', ''.join(tmp))
                print('transition', states[s], j, '2097 -1 1.0')
                #print()
            tmp[j]='0'
        j+=1
        
print('mdptype episodic')
print('discount  1.0')
