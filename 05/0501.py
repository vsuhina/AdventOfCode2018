with open("input.txt") as f:
    inp = f.read().strip()

subs = []

for i in range(ord('a'),ord('z')+1):
    c = str(chr(i))
    subs.append(c.lower() + c.upper())
    subs.append(c.upper() + c.lower())

found = True
while found:
    found = False
    for sub in subs:
        ind = inp.find(sub)
        while ind >= 0:
            found = True
            inp = inp[:ind] + inp[ind+2:]
            ind = inp.find(sub)
print(len(inp))
