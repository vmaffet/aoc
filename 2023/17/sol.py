#!/usr/bin/python3

heatloss = {}
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        heatloss.update(
            {(x,y): int(c) for x, c in enumerate(line.strip())}
        )

width  = max(x for (x,_) in heatloss) + 1
height = max(y for (_,y) in heatloss) + 1

def bestRoute(minTravel, maxTravel):
    queue = [(0, 0, (1,0)), (0, 0, (0,1))]
    dist = {p:0 for p in queue}
    while queue:
        (x, y, (dx,dy)) = queue.pop()
        if x == width-1 and y == height-1:
            return dist[(x, y, (dx,dy))]

        for a in [1,-1]:
            h = dist[(x, y, (dx,dy))]
            for i in range(1, maxTravel+1):
                px, py = x + a*i*dx, y + a*i*dy
                if (px, py) not in heatloss:
                    continue

                h += heatloss[(px,py)]
                if i < minTravel:
                    continue

                np = (px, py, (dy,dx))
                if np in dist:
                    dist[np] = min(dist[np], h)
                else:
                    dist[np] = h
                    queue.append(np)

        queue.sort(key=dist.get, reverse=True)

# ==== Part 1 ==== #
print(bestRoute(1, 3))

# ==== Part 2 ==== #
print(bestRoute(4, 10))
