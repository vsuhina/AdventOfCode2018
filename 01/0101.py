with open("input.txt") as f:
    content = f.readlines()

print(sum(map(int,content)))