with open("input.txt") as f:
    content = f.readlines()

freq = 0
freqlist = [0]
found = False

while not(found):
    for line in content:
        if line[0] == '+':
            freq += int(line[1:])
        elif line[0] == '-':
            freq -= int(line[1:])
        if freq in freqlist:
            print(freq)
            found = True
            break
        else:
            freqlist.append(freq)

print('end')