file = open("dag-2.txt", "r")
horizontaal = 0
verticaal = 0
for line in file.readlines():
    if "forward" in line:
        newline = line.replace("forward", "")
        horizontaal += int(newline)
    elif "up" in line:
        newline = line.replace("up", "")
        verticaal -= int(newline)
    elif "down" in line:
        newline = line.replace("down", "")
        verticaal += int(newline)
print(horizontaal * verticaal)