def react(inp, subs):
    s = str(inp)
    found = True
    while found:
        found = False
        for sub in subs:
            ind = s.find(sub)
            while ind >= 0:
                found = True
                s = s[:ind] + s[ind+len(sub):]
                ind = s.find(sub)
    return s

if __name__ == "__main__":

    with open("input.txt") as f:
        inp = f.read().strip()

    subs = []
    errs = []

    for i in range(ord('a'),ord('z')+1):
        c = str(chr(i))
        subs.append(c.lower() + c.upper())
        subs.append(c.upper() + c.lower())
        errs.append([c.lower(), c.upper()])

    res = []
    for i in range(len(errs)):
        print(i, errs[i])
        s1 = react(inp, errs[i])
        s2 = react(s1, subs)
        res.append(len(s2))

    print(min(res))