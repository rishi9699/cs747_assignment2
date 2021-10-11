import argparse

def decoder_function(value_policy, statefile, player_id):
    f = open(statefile)
    states = f.read().split()
    states = dict(zip(range(len(states)), states))


    print(player_id)

    f = open(value_policy)
    line = f.readline().split()
    actions = [0]*9
    i=0
    while i<len(states):
        print(states[i], end=' ')
        actions[int(line[1])]=1
        print(*actions)
        actions[int(line[1])]=0
        line = f.readline().split()
        i+=1

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--value-policy")
    parser.add_argument("--states")
    parser.add_argument("--player-id")
    args = parser.parse_args()
    decoder_function(args.value_policy, args.states, args.player_id)
