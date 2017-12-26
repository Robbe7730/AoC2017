import collections

class Particle(object):
    a = (0,0,0)
    v = (0,0,0)
    p = (0,0,0)
    _id = 0

    def __init__(self, p, v, a, _id):
        self.p = p
        self.v = v
        self.a = a
        self._id = _id

    def step(self):
        self.v = tuple(map(sum, zip(self.v, self.a)))
        self.p = tuple(map(sum, zip(self.p, self.v)))
        # print(self._id, self.p)
        return self.p

    def getDistance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

with open("input.txt", "r") as file:
    contents = [x.strip() for x in file.readlines()]
    particles = []
    for i, line in enumerate(contents):
        data = [x.strip()[3:-1] for x in line.split(", ")]
        p = tuple([int(x) for x in data[0].split(",")])
        v = tuple([int(x) for x in data[1].split(",")])
        a = tuple([int(x) for x in data[2].split(",")])
        particles.append(Particle(p, v, a, i))

    for i in range(100000):
        universe = collections.defaultdict(list)
        for part in particles:
            pos = part.step()
            universe[pos].append(part)

        for pos in universe:
            curr = universe[pos]
            if(len(curr) > 1):
                for p in curr:
                    particles.remove(p)
        print(len(particles))
