def isvalid():
    file = open('input2.txt', 'r')
    lines = file.readlines()

    invalid_games = set([])
    valid_games = set([])
    for line in lines:
        game_title = line.split(':')[0][5:]
        valid_games.add(int(game_title))
        game = line.split(':')[1].split(';')
        for subgame in game:
            for i in range(len(subgame)): 
                try: 
                    if subgame[i+2] == 'r':
                        if int(subgame[i-1:i+1]) > 12:
                            invalid_games.add(int(game_title))
                        else:
                            pass
                    elif subgame[i+2] == 'b':
                        if int(subgame[i-1:i+1]) > 14:
                            invalid_games.add(int(game_title))
                        else:
                            pass
                    elif subgame[i+2] =='g':
                        if int(subgame[i-1:i+1]) > 13:
                            invalid_games.add(int(game_title))
                        else:
                            pass
                except:
                    pass

    for number in invalid_games:
        valid_games.remove(number)        
    totals = list(valid_games)
    number = sum(totals)

    return number

# print(isvalid())
                
def min_nums():
    file = open('input2.txt', 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        min_red = 0
        min_blue = 0
        min_green = 0
        game = line.split(':')[1].split(';')
        for subgame in game:
            print(subgame)
            for i in range(len(subgame)): 
                try: 
                    if subgame[i+2:i+5] == 'red':
                        if int(subgame[i-1:i+1]) > min_red:
                            min_red = int(subgame[i-1:i+1])
                            print('updated red: ', int(subgame[i-1:i+1]) )
                        else:
                            pass
                    elif subgame[i+2:i+4] == 'bl':
                        if int(subgame[i-1:i+1]) > min_blue:
                            min_blue = int(subgame[i-1:i+1])
                        else:
                            pass
                    elif subgame[i+2:i+7] =='green':
                        if int(subgame[i-1:i+1]) > min_green:
                            min_green = int(subgame[i-1:i+1])
                        else:
                            pass
                except:
                    pass
        print(min_red, min_blue, min_green)
        power = min_red * min_blue * min_green
        total += power

    return total

print(min_nums())
                