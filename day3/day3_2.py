with open("day3.txt",'r') as f:
    lines = f.readlines()

score = 0

rucksacks = [line.strip("\n") for line in lines]

for idx in range(0, len(rucksacks), 3):

    food_type = set(rucksacks[idx]) & set(rucksacks[idx+1]) & set(rucksacks[idx+2]) 

    food_type= ord(list(food_type)[0])
    
    # Lowercase item types a through z have priorities 1 through 26. Unicode a=97, 97-96 =1
    # Uppercase item types A through Z have priorities 27 through 52. Unicode A=65, 65-38 = 27

    if food_type >= 97:
        score += food_type - 96
    else:
        score += food_type -38

print(score)

    

