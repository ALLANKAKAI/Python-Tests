rep = open('animals.txt', 'r+')
read = rep.read()
print(read)


replace = read.replace('dog', 'lion')
op = open('animals.txt', 'w')
new = op.write(replace)
print('New Y:', new)

rep.close()

op = open("animals.txt", "r+")
read2 = op.read()
replace2 = read2.replace("cow", "jogoo")
op.write(replace2)
op.close()
