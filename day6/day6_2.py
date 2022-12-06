with open("input.txt", "r") as f:
    data = f.readlines()

data = ''.join(data)

for i in range(len(data)-13):
    if len(set(data[i:i+14])) == 14:
        print(i+14)
        break