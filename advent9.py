file = open('input9.txt', 'r')
filelist = file.read().split('\n')
filelist = filelist[:len(filelist) - 1]

histories = []
for line in filelist:
    histories.append([[int(x) for x in line.split(' ')]])

for i in range(len(histories)):
    while True:
        curr = histories[i][-1]
        seq = []
        for j in range(len(curr) - 1):
            seq.append(curr[j + 1] - curr[j] )
        histories[i].append(seq)
        if sum(seq) == 0:
            break
    
def pt1(histories):
    total = 0
    for i in range(len(histories)):
        iter = len(histories[i])
        histories[i][iter-1].append(0)
        for j in range(iter - 2, -1, -1):
            histories[i][j].append(histories[i][j+1][-1] + histories[i][j][-1])
        total += histories[i][0][-1]
    return total

# print(pt1(histories))

def pt2(histories):
    total = 0
    for i in range(len(histories)):
        iter = len(histories[i])
        histories[i][-1].append(0)
        for j in range(iter - 2, -1, -1):
            histories[i][j].insert(0, histories[i][j][0] - histories[i][j+1][0])
        total += histories[i][0][0]
    return total

print(pt2(histories))