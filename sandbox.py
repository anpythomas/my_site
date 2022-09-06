# Using readlines()
file1 = open('requirements.txt', 'r')
Lines = file1.readlines()

count = 0
ctr = 0
# Strips the newline character
for line in Lines:
    count += 1

    ctr = 0
    for char in line:
        ctr += 1
        if "@" in line:
            if char == " ":
                print(line[:ctr-1])
                break
        else:
            print(line, end="")
            break

