with open("day3.txt",'r') as f:
    lines = f.readlines()

score = 0

rucksacks = [line.strip("\n") for line in lines]

for rucksack in rucksacks:
    half = len(rucksack)//2

    first = rucksack[:half]
    second = rucksack[half:]

    food_type = set(first) & set(second)
    food_type = list(food_type)[0]
    
    food_type= ord(food_type)
    
    # Lowercase item types a through z have priorities 1 through 26. Unicode a=97, 97-96 =1
    # Uppercase item types A through Z have priorities 27 through 52. Unicode A=65, 65-38 = 27

    if food_type >= 97:
        score += food_type - 96
    else:
        score += food_type -38        

print(score)

    

