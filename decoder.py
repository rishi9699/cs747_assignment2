import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--value-policy")
parser.add_argument("--states")
parser.add_argument("--player-id")

args = parser.parse_args()

f = open(args.states)
states = f.read().split()
states = dict(zip(range(len(states)), states))


print(args.player_id)

f = open(args.value_policy)
line = f.readline().split()
actions = [0]*9
i=0
while len(line)!=0:
    print(states[i], end=' ')
    actions[int(line[1])]=1
    print(*actions)
    actions[int(line[1])]=0
    line = f.readline().split()
    i+=1
    
