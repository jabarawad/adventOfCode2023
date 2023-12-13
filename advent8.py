import math 

def lcm(a):
    lcm = 1
    for i in a:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

def solution():
    file = open('input8.txt', 'r')
    filelist = file.read().split('\n')
    instruct = filelist[0]+filelist[1]
    map = {}

    for i in range(3, len(filelist) - 1):
        x = filelist[i].split(' = ')
        print(x)
        x1 = x[0]
        x2 = x[1].split(',')
        map[x1] = (x2[0][1:4], x2[1][1:4])
    i = 0
    curr = 'AAA'
    counter = 1
    while True:
        if i == len(instruct):
            i = 0
        if instruct[i] == 'L':
            curr = map[curr][0]
        elif instruct[i] == 'R': 
            curr = map[curr][1]
        
        if curr == 'ZZZ':
            return counter
        i += 1
        counter += 1

# print(solution())

def solution2():
    file = open('input8.txt', 'r')
    filelist = file.read().split('\n')
    instruct = filelist[0] + filelist[1]
    map = {}

    for i in range(2, len(filelist) - 1):
        x = filelist[i].split(' = ')
        x1 = x[0]
        x2 = x[1].split(',')
        map[x1] = (x2[0][1:4], x2[1][1:4])
    
    i = 0
    curr = []
    for node in map:
        if node[-1] == 'A':
            curr.append(node)
    counter = [0 for node in curr]
    while True:
        if i == len(instruct):
            i = 0
        if instruct[i] == 'L':
            for j in range(len(curr)):
                if curr[j][-1] != 'Z':
                    curr[j] = map[curr[j]][0]
                    counter[j] += 1
        elif instruct[i] == 'R': 
            for k in range(len(curr)):
                if curr[k][-1] != 'Z':
                    curr[k] = map[curr[k]][1]
                    counter[k] += 1
        check = ''
        for node in curr:
            check += node[-1]
        if check == ('Z' * len(curr)):
            return counter
        i += 1

print(lcm(solution2()))
