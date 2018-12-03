with open("input.txt") as f:
    content = f.readlines()

freq = 0
freqset = set([0])
found = False

while not(found):
    for line in content:
        freq += int(line)
        if freq in freqset:
            print(freq)
            found = True
            break
        else:
            freqset.add(freq)