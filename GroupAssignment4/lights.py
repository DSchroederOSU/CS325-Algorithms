#!/usr/bin/python

from cnf2sat import satisfiable

with open('input.txt', 'r') as f:
    first = f.readline().strip('\n').split(',')
    num_switches = int(first[0])
    num_lights = int(first[1])
    conditions = [int(pos) for pos in f.readline().strip('\n').split(',')]


    switches = [[0 for i in range(num_switches)] for j in range(num_lights)]

    for i in range(0, num_switches):
        for light in f.readline().strip('\n').split(','):
            switches[int(light)-1][i] = 1
    f.close()


CFN = []  # store the series of 2-CNF statements as tuples

#### s1 --- L1 ---- s2

#### RULE #1
#### if L1 is on ---> CNF = (s1, s2), (-s1, -s2)
#### Force one switch to be true and one to be false

#### RULE #2
#### if L1 is off ---> CNF = (s1, -s2), (-s1, s2)
#### Force both swicthes to be true or both be false

# 1 => switch is attached to light, 0 otherwise
# there will be 2 "1's" per row (light); each light has exactly two switches
#      n (num_switches)
#   [(0/1), (0/1), (0/1)]
#   [(0/1), (0/1), (0/1)]
# m [(0/1), (0/1), (0/1)]
#   [(0/1), (0/1), (0/1)]
#   [(0/1), (0/1), (0/1)]


for x in range(0, num_lights):
    # get current light's connecting switches
    light_vals = [index+1 for index, switch in enumerate(switches[x]) if switch == 1]

    # if the light is on, apply Rule #1
    if conditions[x] == 1:
        CFN.append((light_vals[0], light_vals[1]))
        CFN.append((light_vals[0]*-1, light_vals[1]*-1))
    # if the light is off, apply Rule #2
    else:
        CFN.append((light_vals[0] * -1, light_vals[1]))
        CFN.append((light_vals[0], light_vals[1] * -1))

with open("output.txt", "w+") as out:
    if satisfiable(CFN):
        out.write("yes")
    else:
        out.write("no")
    out.close()

exit(0)
