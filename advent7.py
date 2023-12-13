def count_occurrences(c, card):
    s = 0
    e = len(card) - 1
    o = 0
    while s <= e:  
        if card[s] == c:
            o += 1
        if card[e] == c and e != s:
            o += 1
        s += 1
        e -= 1
    return o

def cardscore(card):
    total = 0
    e = set([c for c in card])
    ord = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    
    if len(e) == 1:
        total += 7000000000000000000000000
    elif len(e) == 2:
        o = count_occurrences(card[0], card) 
        if o == 1 or o == 4:
            total += 6000000000000000000000000
        else: total += 5000000000000000000000000
    elif len(e) == 3:
        if count_occurrences(list(e)[0], card) == 3 or count_occurrences(list(e)[1], card) == 3 or count_occurrences(list(e)[2], card) == 3:
            total += 4000000000000000000000000
        else:
            total += 3000000000000000000000000
    elif len(e) == 4:
        total += 2000000000000000000000000
    else:
        total += 1000000000000000000000000
    total += ord[card[0]] * 100000000 + ord[card[1]] * 1000000 + ord[card[2]] * 10000 + ord[card[3]] * 100 + ord[card[4]] * 1

    return total

def solution():
    file = open('input7.txt', 'r')
    filelist = file.read().split('\n')
    h = []
    b = []
    r = []
    
    for x in filelist:
        xs = x.split(' ')
        h.append(xs[0])
        b.append(int(xs[1]))
    total = [0 for c in range(len(h))]
    for x in range(len(h)):
        r.append((cardscore(h[x]), x))
    r.sort(key=lambda x: x[0], reverse=True)
    r = list(map(lambda x: x[1], r ))

    for p in range(len(r)):
        total[r[p]] += (len(r)-p) * b[r[p]]
    
    print(sum(total))

# solution()

def cardscore2(card):
    total = 0
    e = set([c for c in card])
    ord = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J': 1}
    js = count_occurrences('J', card)
    if len(e) == 1:
        total += 7000000000000000000000000
    elif len(e) == 2:
        o = count_occurrences(card[0], card) 
        if js > 0:
            total += 7000000000000000000000000
        else:
            if o == 1 or o == 4:
                total += 6000000000000000000000000
            else: 
                total += 5000000000000000000000000
    elif len(e) == 3:
        if js > 0:
            if js == 3 or js == 2:
                total += 6000000000000000000000000
            elif js == 1:
                for char in card:
                    if char != 'J':
                        o = count_occurrences(char, card)
                        if o == 1:
                            total += 6000000000000000000000000
                        elif o == 2:
                            total += 5000000000000000000000000
                        elif o == 3:
                            total += 6000000000000000000000000
                        break
        elif count_occurrences(list(e)[0], card) == 3 or count_occurrences(list(e)[1], card) == 3 or count_occurrences(list(e)[2], card) == 3:
            total += 4000000000000000000000000
        else:
            total += 3000000000000000000000000
    elif len(e) == 4:
        if js > 0:
            total += 4000000000000000000000000
        else:
            total += 2000000000000000000000000
    else:
        if js == 1:
            total += 2000000000000000000000000
        else:
            total += 1000000000000000000000000
    total += ((ord[card[0]] * 10000000000) + (ord[card[1]] * 100000000) + (ord[card[2]] * 1000000) + (ord[card[3]] * 10000) + (ord[card[4]] * 100))
    return total

def solution2():
    file = open('input7.txt', 'r')
    filelist = file.read().split('\n')
    h = []
    b = []
    r = []
    for x in filelist:
        xs = x.split(' ')
        h.append(xs[0])
        b.append(int(xs[1]))
    total = [0 for c in range(len(h))]
    for x in range(len(h)):
        r.append((cardscore2(h[x]), x, h[x]))
    r.sort(key=lambda x: x[0], reverse=True)
    r = list(map(lambda x: x[1], r ))
    for p in range(len(r)):
        total[r[p]] += (len(r)-p) * b[r[p]]
    print(sum(total))

solution2()

# assert cardscore('AAAAA') > cardscore('AAAAK')
# assert cardscore('AAAAA') > cardscore('22222')
# assert cardscore('AAKKK') > cardscore('AKAAK')
# assert cardscore('AKAKK') > cardscore('KKAAA')
# assert cardscore('2AAAA') > cardscore('AAAKK')
# assert cardscore('2AAAA') < cardscore('AAAAK')
# assert cardscore('AAAA2') > cardscore('KAAAA')
# assert cardscore('A2AAA') > cardscore('KAAAA')
# assert cardscore('AA2AA') > cardscore('AKAAA')
# assert cardscore('AAA2A') > cardscore('AAKAA')
# assert cardscore('AAAA2') > cardscore('AAAKA')
# assert cardscore('AAAA2') < cardscore('AAAAK')
# assert cardscore('AAAA2') < cardscore('AAAA3')
# assert cardscore('AKAK2') > cardscore('AKQJ98')
# assert cardscore('AKKAK') > cardscore('KKKAA')
# assert cardscore('AAAKK') > cardscore('AAKKJ')
# assert cardscore('AKAKA') > cardscore('AAKKJ')
# assert cardscore('AAKQJ') < cardscore('A232A')
# assert cardscore('AAA23') < cardscore('22223')

# assert cardscore2('AAA23') < cardscore2('22223')
# assert cardscore2('JJJAA') < cardscore2('AAAAA')
# assert cardscore2('JJJAA') > cardscore2('AAAAK')
# assert cardscore2('AKQJQ') > cardscore2('QKAAA')
# assert cardscore2('QQQJA') < cardscore2('KTJJT')
# assert cardscore2('J2345') < cardscore2('22345')
# assert cardscore2('J2345') > cardscore2('62345')
# assert cardscore2('K23JJ') < cardscore2('K23KK')
# assert cardscore2('KK3JJ') > cardscore2('22223')
# assert cardscore2('AAAAJ') > cardscore2('AAAAK')
# assert cardscore2('TJT2K') < cardscore2('22233')
# assert cardscore2('TJT2K') > cardscore2('3K323')



















