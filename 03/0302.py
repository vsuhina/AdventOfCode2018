import re

class Claim:
    regex = "#([\d]+) @ ([\d]+),([\d]+): ([\d]+)x([\d]+)"

    def __init__(self, inp):
        m = re.search(self.regex, inp)
        self.id = int(m.group(1))
        self.left = int(m.group(2))
        self.top = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))

    def __str__(self):
        return "ID:{0} POS:{1},{2} SIZE:{3},{4}".format(self.id, self.left, self.top, self.width, self.height)

if __name__ == "__main__":

    with open("input.txt") as f:
        claims = [Claim(l.strip()) for l in f.readlines()]

    maxwidth = max(map(lambda c: c.left + c.width, claims))
    maxheight = max(map(lambda c: c.top + c.height, claims))
    print(maxwidth, maxheight)

    # make fabric (all zeros)
    fabric = []
    for i in range(maxwidth):
        fabric.append([])
        for j in range(maxheight):
            fabric[i].append(0)

    # add on each field claim count
    for c in claims:
        for i in range (c.left, c.left + c.width):
            for j in range (c.top, c.top + c.height):
                fabric[i][j] += 1

    # search for claim that has all the fields set at 1
    for c in claims:
        overlaps = False
        for i in range (c.left, c.left + c.width):
            for j in range (c.top, c.top + c.height):
                if fabric[i][j] > 1:
                    overlaps = True
        if not(overlaps):
            print(c.id)