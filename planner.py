import argparse
import pulp as p
import numpy as np

def planner_function(mdplocation, algorithm='vi'):
    f = open(mdplocation)
    a = f.readline()
    ns = int(a.split()[1])
    a = f.readline()
    na = int(a.split()[1])
    a = f.readline()
    end_state = (a.split())[1:]
    end_state = np.array(end_state, dtype='int')

    mdp = dict(zip(range(ns), [dict() for _ in range(ns)]))
    tl = f.readline().split()
    while tl[0]=='transition':
        if int(tl[2]) in mdp[int(tl[1])]:
            mdp[int(tl[1])][int(tl[2])].append( [int(tl[3]), float(tl[4]), float(tl[5])] )
        else:
            mdp[int(tl[1])][int(tl[2])] = [[int(tl[3]), float(tl[4]), float(tl[5])]]
        tl = f.readline().split()
        

    gamma = float((f.readline().split())[1])

    if algorithm=='vi':
        V=np.zeros(ns)
        acts = np.zeros(ns, dtype='int')
        condition = True
        while condition:
            prev_v = V.copy()
            for s in range(ns):
                if s in end_state:
                    continue

                action = next(iter(mdp[s]))
                cursum = 0
                for sp in mdp[s][action]:
                    cursum+= sp[2]*(sp[1] + gamma*V[sp[0]])
                val = cursum
                
                for a in mdp[s].keys():
                    cursum = 0
                    for sp in mdp[s][a]:
                        cursum+= sp[2]*(sp[1] + gamma*V[sp[0]])
                    if cursum>val:
                        val=cursum
                        action=a
                V[s] = val
                acts[s] = action
            condition = True if max(abs(V-prev_v))>0.000000000001 else False
            
        for i in range(ns):
            print("{:.6f}".format(V[i]), acts[i])

    if algorithm=='hpi':
        V=np.zeros(ns)
        acts = np.zeros(ns, dtype='int')
        for i in range(ns):
            if i in end_state:
                continue
            acts[i] = next(iter(mdp[i]))
            
        def update_v(acts, V):
            condition = True
            while condition:
                prev_v = V.copy()
                for s in range(ns):
                    if s in end_state:
                        continue
                    cursum=0
                    for sp in mdp[s][acts[s]]:
                        cursum+= sp[2]*(sp[1] + gamma*V[sp[0]])
                    V[s] = cursum
                condition = True if max(abs(V-prev_v))>0.000000000001 else False
            
        condition = True
        while condition:
            prev_acts = acts.copy()
            for s in range(ns):
                if s in end_state:
                    continue
                
                max_a = next(iter(mdp[s]))
                cursum = 0
                for sp in mdp[s][max_a]:
                    cursum+= sp[2]*(sp[1] + gamma*V[sp[0]])
                val = cursum
            
                for a in mdp[s].keys():    
                    cursum = 0
                    for sp in mdp[s][a]:
                        cursum+= sp[2]*(sp[1] + gamma*V[sp[0]])
                    if cursum>val:
                        max_a = a
                        val=cursum
                acts[s] = max_a
            update_v(acts, V)
            condition = True if sum(prev_acts-acts)!=0 else False
            
        for i in range(ns):
            print("{:.6f}".format(V[i]), acts[i])

    if algorithm=='lp':
        
        V = p.LpVariable.dicts("V", range(ns))
        
        # The objective function
        Lp_prob = p.LpProblem('Problem', p.LpMinimize)
        exp = 0
        for i in V.values():
            exp+=i
        Lp_prob+= exp
        
        #Constraints
        for s in range(ns):
            if s in end_state:
                Lp_prob += V[s] == 0
                continue
            for a in mdp[s].keys():
                exp = 0
                for sp in mdp[s][a]:
                    exp+= sp[2]*(sp[1] + gamma*V[sp[0]])
                Lp_prob += V[s] >= exp
                
        soln_status = p.GLPK_CMD(msg=False).solve(Lp_prob)
        
        acts = np.zeros(ns, dtype='int')
        
        for s in range(ns):
            if s in end_state:
                continue
            
            a = next(iter(mdp[s]))
            cursum = 0
            for sp in mdp[s][a]:
                cursum+= sp[2]*(sp[1] + gamma*(V[sp[0]].value()))
            max_a = a
            val = cursum
            
            for a in mdp[s].keys():
                cursum = 0
                for sp in mdp[s][a]:
                    cursum+= sp[2]*(sp[1] + gamma*(V[sp[0]].value()))
                if cursum>val:
                    max_a = a
                    val=cursum
            acts[s] = max_a
            
        for i in range(ns):
            print("{:.6f}".format(V[i].value()), acts[i])


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mdp")
    parser.add_argument("--algorithm", default='vi')
    args = parser.parse_args()
    planner_function(args.mdp, args.algorithm)
