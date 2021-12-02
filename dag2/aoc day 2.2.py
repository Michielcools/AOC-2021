file = open("dag-2.txt", "r")
horizontaal = 0
aim = 0
verticaal = 0
for line in file.readlines():
    if "forward" in line:
        newline = line.replace("forward", "")
        horizontaal += int(newline)
        verticaal += int(newline) * aim
    elif "up" in line:
        newline = line.replace("up", "")
        aim -= int(newline)
    elif "down" in line:
        newline = line.replace("down", "")
        aim += int(newline)
print(horizontaal * verticaal)