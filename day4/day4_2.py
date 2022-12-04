import re

with open("day4.txt", "r") as f:
    lines = f.readlines()

ct = 0    

for line in lines:
    line = line.strip("\n") #['17-99,18-24']
    line = re.split(',|-', line) #['17', '99', '18', '24']

    num1, num2, num3, num4 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
    
    condition1 = num2 < num3
    condition2 = num4 < num1

    if not(condition1 or condition2):

        ct += 1

print(ct)