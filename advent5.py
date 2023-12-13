import math

def solution():
    file = open('input5.txt', 'r')
    lines = file.readlines()
    table = []

    to_concat = []
    for line in lines:
        if 'map' not in line:
            to_concat.append(line[:len(line) - 1].split())
        else:
            table.append(to_concat)
            to_concat = [line[:len(line) - 1]]
    table.append(to_concat)
    seeds = table[0][0][1:]
    seed_to_soil = table[1][1:]
    soil_to_fertilizer = table[2][1:]
    fertilizer_to_water = table[3][1:]
    water_to_light = table[4][1:]
    light_to_temp = table[5][1:]
    temp_to_humidity = table[6][1:]
    humidity_to_location = table[7][1:]
    print(table)
    location_nums = []
    for seed in seeds:
        soil = False
        fertilizer = False
        water = False
        light = False
        temp = False
        humidity = False
        location = False
        
        for mapping in seed_to_soil:
            soil = helper(seed, mapping[0], mapping[1], mapping[2])
            if soil != False:
                break
        if soil == False:
            soil = seed

        for mapping in soil_to_fertilizer:
            fertilizer = helper(soil, mapping[0], mapping[1], mapping[2])
            if fertilizer != False:
                break
        if fertilizer == False:
            fertilizer = soil

        for mapping in fertilizer_to_water:
            water = helper(fertilizer, mapping[0], mapping[1], mapping[2])
            if water != False:
                break
        if water == False:
            water = fertilizer

        for mapping in water_to_light:
            light = helper(water, mapping[0], mapping[1], mapping[2])
            if light != False:
                break
        if light == False:
            light = water

        for mapping in light_to_temp:
            temp = helper(light, mapping[0], mapping[1], mapping[2])
            if temp != False:
                break
        if temp == False:
            temp = light

        for mapping in temp_to_humidity:
            humidity = helper(temp, mapping[0], mapping[1], mapping[2])
            if humidity != False:
                break
        if humidity == False:
            humidity = temp

        for mapping in humidity_to_location:
            location = helper(humidity, mapping[0], mapping[1], mapping[2])
            if location != False:
                break
        if location == False:
            location = humidity

        location_nums.append(location)
    
    least = float('inf')
    for loc in location_nums:
        if loc < least:
            least = loc
    print(least) 

def helper(seed, dest, source, increment):
    if (int(seed) >= int(source)) and (int(seed) <= (int(source) + int(increment))):
        return (int(dest) + (int(seed) - int(source)))
    return False

# solution()

def solution2():
    file = open('input5.txt', 'r')
    lines = file.readlines()
    table = []

    to_concat = []
    for line in lines:
        if 'map' not in line:
            to_concat.append(line[:len(line) - 1].split())
        else:
            table.append(to_concat)
            to_concat = [line[:len(line) - 1]]
    table.append(to_concat)

    seeds = table[0][0][1:]
    newseeds = []
    mappings = {}
    for i in range(len(seeds)):
        if i%2 == 0:
            newseeds.append(seeds[i])
            mappings[seeds[i]] = []
        else:
            for j in range(1, int(seeds[i]), int(seeds[i]) - 1):
                newseeds.append(str(int(seeds[i-1]) + j))
                mappings[str(int(seeds[i-1]) + j)] = []

    seed_to_soil = table[1][1:]
    soil_to_fertilizer = table[2][1:]
    fertilizer_to_water = table[3][1:]
    water_to_light = table[4][1:]
    light_to_temp = table[5][1:]
    temp_to_humidity = table[6][1:]
    humidity_to_location = table[7][1:]

    location_nums = []
    for seed in newseeds:
        soil = False
        fertilizer = False
        water = False
        light = False
        temp = False
        humidity = False
        location = False
        
        for mapping in seed_to_soil:
            soil = helper(seed, mapping[0], mapping[1], mapping[2])
            if soil != False:
                break
        if soil == False:
            soil = seed
        mappings[seed] = [soil]

        for mapping in soil_to_fertilizer:
            fertilizer = helper(soil, mapping[0], mapping[1], mapping[2])
            if fertilizer != False:
                break
        if fertilizer == False:
            fertilizer = soil
        mappings[seed].append(fertilizer)

        for mapping in fertilizer_to_water:
            water = helper(fertilizer, mapping[0], mapping[1], mapping[2])
            if water != False:
                break
        if water == False:
            water = fertilizer
        mappings[seed].append(water)

        for mapping in water_to_light:
            light = helper(water, mapping[0], mapping[1], mapping[2])
            if light != False:
                break
        if light == False:
            light = water
        mappings[seed].append(light)


        for mapping in light_to_temp:
            temp = helper(light, mapping[0], mapping[1], mapping[2])
            if temp != False:
                break
        if temp == False:
            temp = light
        mappings[seed].append(temp)


        for mapping in temp_to_humidity:
            humidity = helper(temp, mapping[0], mapping[1], mapping[2])
            if humidity != False:
                break
        if humidity == False:
            humidity = temp
        mappings[seed].append(humidity)

        for mapping in humidity_to_location:
            location = helper(humidity, mapping[0], mapping[1], mapping[2])
            if location != False:
                break
        if location == False:
            location = humidity
        mappings[seed].append(location)

        location_nums.append(location)
    
    least = float('inf')
    for loc in location_nums:
        if loc < least:
            least = loc

    for seed in mappings:
        if mappings[seed][-1] == least:
            rel_seed = seed
            print(rel_seed)
    
    newseeds2 = []
    for i in range(3107439672, 3107439673, 1):
        newseeds2.append(i)

    location_nums = []
    for seed in newseeds2:
        soil = False
        fertilizer = False
        water = False
        light = False
        temp = False
        humidity = False
        location = False
        
        for mapping in seed_to_soil:
            soil = helper(seed, mapping[0], mapping[1], mapping[2])
            if soil != False:
                break
        if soil == False:
            soil = seed
        mappings[seed] = [soil]

        for mapping in soil_to_fertilizer:
            fertilizer = helper(soil, mapping[0], mapping[1], mapping[2])
            if fertilizer != False:
                break
        if fertilizer == False:
            fertilizer = soil
        mappings[seed].append(fertilizer)

        for mapping in fertilizer_to_water:
            water = helper(fertilizer, mapping[0], mapping[1], mapping[2])
            if water != False:
                break
        if water == False:
            water = fertilizer
        mappings[seed].append(water)

        for mapping in water_to_light:
            light = helper(water, mapping[0], mapping[1], mapping[2])
            if light != False:
                break
        if light == False:
            light = water
        mappings[seed].append(light)


        for mapping in light_to_temp:
            temp = helper(light, mapping[0], mapping[1], mapping[2])
            if temp != False:
                break
        if temp == False:
            temp = light
        mappings[seed].append(temp)


        for mapping in temp_to_humidity:
            humidity = helper(temp, mapping[0], mapping[1], mapping[2])
            if humidity != False:
                break
        if humidity == False:
            humidity = temp
        mappings[seed].append(humidity)

        for mapping in humidity_to_location:
            location = helper(humidity, mapping[0], mapping[1], mapping[2])
            if location != False:
                break
        if location == False:
            location = humidity
        mappings[seed].append(location)

        location_nums.append(location)

       
    
    least = float('inf')
    for loc in location_nums:
        if loc < least:
            least = loc
    print(least)

    for seed in mappings:
        if mappings[seed][-1] == least:
            rel_seed = seed
            print(rel_seed)

def helper(seed, dest, source, increment):
    if (int(seed) >= int(source)) and (int(seed) <= (int(source) + int(increment))):
        return (int(dest) + (int(seed) - int(source)))
    return False

solution2()

