# build graph of neighbors and candidates
#   - you already have a most
# test midpoints of all candidate pairs and using math,
#    see what component sizes you can make

import math

class Tower:

    def __init__ (self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.component = -1
        self.neighbors = []
        self.candidates = []

    def count_component (self, c):
        self.component = c
        count = 1
        for tower in self.neighbors:
            if tower.component < 0:
                count += tower.count_component(c)
        return count

n = int(input().strip())
most = 0
c = 0
sizes = [0 for size in range(n)]
used = [False for used in range(n)]

def test (t, x, y):
    global most
    towers = sizes[t.component]
    used[t.component] = True
    for t1 in t.candidates:
        if t1.index > t.index and not used[t1.component]:
            if math.hypot(t1.y-y, t1.x-x) < 2:
                used[t1.component] = True
                towers += sizes[t1.component]
    used[t.component] = False
    for t1 in t.candidates:
        if used[t1.component]:
            used[t1.component] = False
    if towers>most:
        most = towers


towers = [0 for x in range(n)]
for i in range(n):
    x, y = [float(x) for x in (input().strip().split())]
    towers[i] = Tower(i,x,y)

for i in range(n):
    for j in range(i):
        distance = math.hypot(towers[i].x-towers[j].x, towers[i].y-towers[j].y)
        if distance < 2:
            towers[i].neighbors.append(towers[j])
            towers[j].neighbors.append(towers[i])
        elif distance < 4:
            towers[i].candidates.append(towers[j])
            towers[j].candidates.append(towers[i])

for tower in towers:
    if tower.component < 0:
        sizes[c] = tower.count_component(c)
        if sizes[c] > most:
            most = sizes[c]
        c += 1

for t1 in towers:
    for t2 in t1.candidates:
        if t2.index > t1.index:
            ydif, xdif = t2.y-t1.y, t2.x-t1.x
            distance, theta = math.hypot(ydif,xdif), math.atan2(ydif,xdif)
            psi = math.acos(distance/4.0)
            test(t1, t1.x + 2.0*math.cos(theta+psi), t1.y + 2.0*math.sin(theta+psi))
            test(t1, t1.x + 2.0*math.cos(theta-psi), t1.y + 2.0*math.sin(theta-psi))

print (most + 1)
