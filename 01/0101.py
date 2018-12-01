with open("input.txt") as f:
    content = f.readlines()

freq = 0

for line in content:
    if line[0] == '+':
        freq += int(line[1:])
    elif line[0] == '-':
        freq -= int(line[1:])

print(freq)