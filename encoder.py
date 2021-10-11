import numpy as np
import argparse


def encoder_function(policyfile, statefile):

    f = open(statefile)
    states = f.read().split()
    states = dict(zip(states, range(len(states))))

    f = open(policyfile)
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
                                    print('transition', states[s], j, states[''.join(tmp)], str(0), probs[k])
                                else:
                                    print('transition', states[s], j, len(states)+1, '1', probs[k])
                                tmp[k]='0'
                            k+=1
                    else:
                        print('transition', states[s], j, len(states), '-1 1.0')
                    tmp[j]='0'
                j+=1
                


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
                                    print('transition', states[s], j, states[''.join(tmp)], str(0), probs[k])
                                else:
                                    if '0' in tmp:
                                        print('transition', states[s], j, len(states)+1, '1', probs[k]) #won
                                    else:
                                        if check1pattern(tmp):
                                            print('transition', states[s], j, len(states)+1, '1', probs[k]) #won
                                        else:
                                            print('transition', states[s], j, len(states), '-1', probs[k]) #draw
                                tmp[k]='0'
                            k+=1
                    else:
                        print('transition', states[s], j, len(states), '-1 1.0')
                    tmp[j]='0'
                j+=1

    print('mdptype episodic')
    print('discount  1.0')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy")
    parser.add_argument("--states")
    args = parser.parse_args()
    encoder_function(args.policy, args.states)
