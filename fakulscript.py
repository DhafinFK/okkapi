file1 = open('fakultas.txt', 'r')
lines = file1.readlines()

for line in lines:
    line = line.strip('\n')
    line = line.split('&')
    line[0] = line[0].replace("_", " ")
    print(line)