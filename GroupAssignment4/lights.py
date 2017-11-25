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


CFN = []
for x in range(0, num_lights):
    light_vals = switches[x]
    light_switches = []
    for y in range(0, len(light_vals)):
        if light_vals[y] == 1:
            light_switches.append(y+1)
    if conditions[x] == 1:  # if the light is on, make sure only one switch gets hit
        CFN.append((light_switches[0], light_switches[1]))
        CFN.append((light_switches[0]*-1, light_switches[1]*-1))
    else:  # if the light is off, both switches or neither switch must be hit
        CFN.append((light_switches[0] * -1, light_switches[1]))
        CFN.append((light_switches[0], light_switches[1] * -1))

print(CFN)
print(satisfiable(CFN))

with open("output.txt", "w+") as out:
    if satisfiable(CFN):
        out.write("yes")
    else:
        out.write("no")
    out.close()

exit(0)
