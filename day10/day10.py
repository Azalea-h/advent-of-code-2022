# part 1 answer 15220

with open("input.txt", "r") as f:
    lines = f.readlines()

instructions = [line.strip().split() for line in lines]

cycle = 1
x = 1
checks = [20, 60, 100, 140, 180, 220]
score = 0
i = 0

while cycle <= 220 and i < len(instructions):

    instruction = instructions[i]

    if cycle in checks:
        score += cycle * x

    if instruction[0] =="addx": 
        cycle += 1
        
        if cycle in checks:
            score += cycle * x
        
        cycle += 1
        x += int(instruction[-1])
 
    else: # noop
        cycle += 1   
   
    i += 1

print(score)