def solution():
    file = open('input6.txt', 'r')
    filelist = file.read().split('\n')
    t = [int(y) for y in filelist[0].split()[1:]]
    d = [int(x) for x in filelist[1].split()[1:]]

    n = len(t)
    total = 1
    for i in range(n):
        dists = []
        count = 0
        for j in range(t[i]):
            dists.append((t[i] - j) * j)
        for dist in dists:
            if dist > d[i]:
                count += 1
        if count > 0:
            total *= count
    if total == 1:
        print(0)
    else:
        print(total)

solution()

def solution2():
    file = open('input6.txt', 'r')
    filelist = file.read().split('\n')
    t = int("".join([y for y in filelist[0].split()[1:]]))
    d = int("".join([x for x in filelist[1].split()[1:]]))

    dists = []
    count = 0
    for i in range(t):
        dists.append((t - i) * i)
    for dist in dists:
        if dist > d:
            count += 1
    print(count)

solution2()
    