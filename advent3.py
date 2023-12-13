
def solution():
    symbols = set(['@','#','$','%','&','*','/','-','+','='])
    file = open('input3.txt', 'r')
    lines = file.readlines()

    total = 0
    field = []
    for line in lines:
        field.append([x for x in line])
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
                if lines[i][j].isdigit():
                    pass
                else:
                    if lines[i][j] != '.' and lines[i][j] != '\n':
                        try:
                            field[i][j-1] = 'X'
                        except:
                            pass
                        try:
                            field[i][j+1] = 'X'
                        except:
                            pass
                        try:
                            field[i+1][j] = 'X'
                        except:
                            pass
                        try:
                            field[i+1][j+1] = 'X'
                        except:
                            pass
                        try:
                            field[i+1][j-1] = 'X'
                        except:
                            pass
                        try:
                            field[i-1][j-1] = 'X'
                        except:
                            pass
                        try:
                            field[i-1][j] = 'X'
                        except:
                            pass
                        try:
                            field[i-1][j+1] = 'X'
                        except:
                            pass
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            temp = ""
            if lines[i][j].isdigit():
                temp += lines[i][j]
                if  lines[i][j+1].isdigit():
                    temp += lines[i][j+1]
                    if lines[i][j+2].isdigit():
                        temp += lines[i][j+2]
                    else:
                        if lines[i][j-1].isdigit():
                            temp = ''
                else:
                    if lines[i][j-1].isdigit():
                        temp = ''
                    
            if temp != '':
                print(temp)
                try:
                    if len(temp) == 1:
                        if field[i][j] == 'X':
                            tempnum = int(temp)
                            total += tempnum
                    if len(temp) == 2:
                        if field[i][j] == 'X' or field[i][j+1] == 'X':
                            tempnum = int(temp)
                            total += tempnum
                            print(tempnum, ' added ')
                            
                    elif len(temp) == 3:
                        if field[i][j] == 'X' or field[i][j+1] == 'X' or field[i][j+2] == 'X':
                            tempnum = int(temp)
                            total += tempnum
                            print(tempnum, ' added')
                except:
                    pass
    return total


# print(solution())

def findnum(matrix, x, y):
    number = ''
    index_start = None
    i = y 
    while matrix[x][i].isdigit() and i >= 0:
        i -= 1
    if not matrix[x][i].isdigit():  
        i += 1
    index_start = i
    while matrix[x][i].isdigit():
        number += matrix[x][i]
        i += 1
    return (number, index_start)
    
def helper(matrix, x, y):
    nums = []
    multiplier = 0

    if matrix[x][y+1].isdigit():
        nums.append(findnum(matrix, x, y+1))
    if matrix[x][y-1].isdigit():
        nums.append(findnum(matrix, x, y-1))
    if matrix[x+1][y].isdigit():
        nums.append(findnum(matrix, x+1, y))
    if matrix[x+1][y+1].isdigit():
        nums.append(findnum(matrix, x+1, y+1))
    if matrix[x+1][y-1].isdigit():
        nums.append(findnum(matrix, x+1, y-1))
    if matrix[x-1][y-1].isdigit():
        nums.append(findnum(matrix, x-1, y-1))
    if matrix[x-1][y+1].isdigit():
        nums.append(findnum(matrix, x-1, y+1))
    if matrix[x-1][y].isdigit():
        nums.append(findnum(matrix, x-1, y))
    
    nums_set = set(nums)
    nums = list(nums_set)

    if len(nums) >= 2:
        multiplier = 1
        for tup in nums:
            multiplier *= int(tup[0])
            
    return multiplier

def solution2():
    file = open('input3.txt', 'r')
    lines = file.readlines()

    matrix = []
    total = 0

    for line in lines:
        matrix.append([x for x in line])

    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == '*':
                total += helper(matrix, i, j)
    
    return total

# print(solution2())