f = open('./pa2_base/pa2_base/data/attt/states/states_file_p2.txt')
states = f.read().split()
states = dict(zip(range(len(states)), states))

f = open('./p2optimalpolicy.txt')
print(1)
i=0
line = f.readline().split()
actions = [0]*9
while len(line)!=0:
    print(states[i], end=' ')
    actions[int(line[1])]=1
    print(*actions)
    actions[int(line[1])]=0
    line = f.readline().split()
    i+=1
    
