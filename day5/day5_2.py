with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n").split(" ") for line in lines]

# ------ search the end of crate list ------

raw_crate_list = []
raw_crate_list_end_searching = True
idx = 0

while raw_crate_list_end_searching:

    if '1' in lines[idx]:
        raw_crate_list_end_searching = False
    else:
        raw_crate_list.append(lines[idx])
        idx+=1

stack_numbers = lines[idx]

stack_numbers = [elm for elm in stack_numbers if elm != ""]
number_of_stacks = len(stack_numbers)

# ------ convert vertical to horizontal ------

nice_crate_list = [[] for crate in range(len(raw_crate_list))] 

for crate_idx in range(len(raw_crate_list)):

    blank_ct = 0

    for stuff_idx in range(len(raw_crate_list[crate_idx])):

        if raw_crate_list[crate_idx][stuff_idx] == "":
            if blank_ct ==0:
                nice_crate_list[crate_idx].append(" ")
                blank_ct += 1
            elif blank_ct == 3:
                blank_ct = 0 
            else:
                blank_ct += 1
        else:
            nice_crate_list[crate_idx].append(raw_crate_list[crate_idx][stuff_idx])

horizontal = [[] for crate in range(number_of_stacks)]

for i in range(len(nice_crate_list)):

    for j in range(len(nice_crate_list[i])):
        if nice_crate_list[i][j] != ' ':
            stuff = nice_crate_list[i][j].replace('[', '').replace(']', '')
            horizontal[j].insert(0, stuff)

# ------ horizontal crate list completed ------

# part2

instructions = lines[idx+2:]

for instruction in instructions:

    num_crate_to_move, from_stack, to_stack = int(instruction[1]), int(instruction[3])-1, int(instruction[5])-1
    stuff_to_move = horizontal[from_stack][-num_crate_to_move:]
    horizontal[from_stack] = horizontal[from_stack][:-num_crate_to_move]
    horizontal[to_stack] += stuff_to_move

for stack in horizontal:

    if len(stack) != 0: 
        print(stack[-1], end="")
    else:
        print("*", end="")

print("\n")
