def summer():
    file1 = open('input1.txt', 'r')
    lines = file1.readlines()
    
    total = []
    for line in lines:
        for i in range(len(line)):
            try:
                num1 = str(int(line[i]))
                break
            except:
                continue
        for j in range(len(line), -1, -1):
            try:
                num2 = str(int(line[j]))
                break
            except:
                continue
        concatted = num1+num2
        total.append(int(concatted))

    return sum(total)

def helper(line):
    myd = {
        'one': 1,
        'two': 2,
        'three':3 ,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for i in range(len(line)):
        try:
            num1 = str(int(line[i]))
            break
        except:
            if line[i:i+3] in myd:
                num1 = str(myd[line[i:i+3]])
                break
            elif line[i:i+4] in myd:
                num1 = str(myd[line[i:i+4]])
                break
            elif line[i:i+5] in myd:
                num1 = str(myd[line[i:i+5]])
                break

    for j in range(len(line), -1, -1):
        try:
            num2 = str(int(line[j]))
            break
        except:
            if line[j-3:j] in myd:
                num2 = str(myd[line[j-3:j]])
                break
            elif line[j-4:j] in myd:
                num2 = str(myd[line[j-4:j]])
                break
            elif line[j-5:j] in myd:
                num2 = str(myd[line[j-5:j]])
                break
    return num1+num2

def helper2(line):
    newline = line.replace('sevenineight', '798')
    newline2 = newline.replace('sevenine','79')
    newline3 = newline2.replace('oneight','18')
    newline4 = newline3.replace('threeight','38')
    newline5 = newline4.replace('fiveight', '58')
    newline6 = newline5.replace('one', '1')
    newline7 = newline6.replace('two', '2')
    newline8 = newline7.replace('three', '3')
    newline9 = newline8.replace('four', '4')
    newline10 = newline9.replace('five', '5')
    newline11 = newline10.replace('six', '6')
    newline12 = newline11.replace('seven', '7')
    newline13 = newline12.replace('eight', '8')
    newline14 = newline13.replace('nine', '9')

    return newline14

def summer2():
    file1 = open('input1.txt', 'r')
    lines = file1.readlines()

    total = []
    for line in lines:
        total.append(int(helper(line)))
    return total

def summer3():
    file1 = open('input1.txt', 'r')
    lines = file1.readlines()

    total = []
    for line in lines:
        newline = helper2(line)
        for i in range(len(newline)):
            try:
                num1 = str(int(newline[i]))
                break
            except:
                continue
        for j in range(len(newline), -1, -1):
            try:
                num2 = str(int(newline[j]))
                break
            except:
                continue
        total.append( int(num1 + num2) )
    return total

try1 = summer2()

try2 = summer3()

for i in range(len(try1)):
    if try1[i] != try2[i]:
        print(i, try1[i], try2[i])