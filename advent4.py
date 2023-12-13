def solution():
    file = open('input4.txt', 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        mult = 0
        values = line.split(':')[1]
        winning_vals = values.split('|')[0]
        elfs_vals = values.split('|')[1]

        winning_vals = winning_vals.split()
        elfs_vals = elfs_vals.split()

        winning_vals = [int(x) for x in winning_vals]
        winning_vals = set(winning_vals)

        for num in elfs_vals:
            if int(num) in winning_vals:
                if mult != 0:
                    mult *= 2
                else:
                    mult = 1
        total += mult
    return total

# print(solution())

def solution2():
    file = open('input4.txt', 'r')
    lines = file.readlines()

    copies = [1 for i in range(len(lines))]
    idx = 0
    for line in lines:
        matches = 0
        values = line.split(':')[1]
        winning_vals = values.split('|')[0]
        elfs_vals = values.split('|')[1]

        winning_vals = winning_vals.split()
        elfs_vals = elfs_vals.split()

        winning_vals = [int(x) for x in winning_vals]
        winning_vals = set(winning_vals)

        for num in elfs_vals:
            if int(num) in winning_vals:
                matches += 1

        for j in range(1, matches+1):
            copies[idx+j] += 1*copies[idx]
        idx += 1
    return sum(copies)

# print(solution2())