import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--policy")
parser.add_argument("--states")
args = parser.parse_args()

f = open(args.states)
states = f.read().split()
states = dict(zip(states, range(len(states))))

f = open(args.policy)
fixedplayer = f.readline()

oppo_acts = {}
tmp = f.readline()
while tmp!='':
    oppo_acts[tmp.split()[0]] = list(np.array(tmp.split()[1:], dtype='float'))
    tmp = f.readline()
    
print('numStates', len(states)+2)
print('numActions 9')
print('end', len(states), len(states)+1)
    
if fixedplayer[0]=='2':
    # big change for p1 code

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
    

if fixedplayer[0]=='1':

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
                                print(s, ''.join(tmp))
                                print('transition', states[s], j, states[''.join(tmp)], str(0), probs[k])
                                print()
                            else:
                                # go to win state
                                print('player 1 ended the game, player 2 won or draw', s, ''.join(tmp))
                                if '0' in tmp:
                                    print('transition', states[s], j, '2424 1', probs[k]) #won
                                else:
                                    if check1pattern(tmp):
                                        print('transition', states[s], j, '2424 1', probs[k]) #won
                                    else:
                                        print('transition', states[s], j, '2423 -1', probs[k]) #draw
                                print()
                            tmp[k]='0'
                        k+=1
                else:
                    # go to draw or lose state and reward 0
                    print(s,'player 2 did something foolish, player 1 won', ''.join(tmp))
                    print('transition', states[s], j, '2423 -1 1.0')
                    print()
                tmp[j]='0'
            j+=1

print('mdptype episodic')
print('discount  1.0')
