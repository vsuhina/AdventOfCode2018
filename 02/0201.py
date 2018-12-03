with open("input.txt") as f:
    content = f.readlines()

count2 = 0
count3 = 0

for line in content:
    c2 = 0
    c3 = 0
    for c in list(set(line)):
        if line.count(c) == 2:
            c2 = 1
        elif line.count(c) == 3:
            c3 = 1
    count2 += c2
    count3 += c3

print (count2 * count3)
