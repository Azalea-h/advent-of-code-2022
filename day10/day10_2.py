def draw(cycle): # return a symbol to add to crt

    global sprite_start
    global sprite_end
    
    position = cycle % 40

    if position >= sprite_start and position <= sprite_end:
        print("#")
        return "#"
    else:
        print(".")
        return "."

with open("input.txt", "r") as f:
    lines = f.readlines()

instructions = [line.strip().split() for line in lines]

sprite_start = 0
sprite_end = sprite_start + 2

cycle = 0
x = 1
checks = [40, 80, 120, 160, 200, 240]

i = 0
screen = []
crt = []

while cycle <= 240 and i < len(instructions):

    instruction = instructions[i]
   
    if cycle in checks:
        screen.append(crt)
        crt = []

    if instruction[-1] == "noop":
        crt.append(draw(cycle))
        cycle += 1
            
    else: # addx
        print("cycle: ", cycle)
        crt.append(draw(cycle))
        cycle += 1

        if cycle in checks:
            screen.append(crt)
            crt = []

        crt.append(draw(cycle))

        sprite_start += int(instruction[-1])
        sprite_end = sprite_start + 2
        cycle += 1
        
    i += 1

for i in screen:
    print("".join(i))
    
        
        
            
            




