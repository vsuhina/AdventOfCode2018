with open("input.txt") as f:
    content = f.readlines()

match = False

for i in range(len(content)):
    line1 = content[i]
    for j in range(i+1, len(content)):
        line2 = content[j]
        similar = True
        mismatch = 0
        for k in range(len(line1)):
            if line1[k] != line2[k]:
                mismatch +=1
            if mismatch > 1:
                break
        if mismatch == 1:
            match = True
            break
    if match:
        break

res = ''

for i in range(len(line1)):
    if line1[i] == line2[i]:
        res += line1[i]

print(res)







