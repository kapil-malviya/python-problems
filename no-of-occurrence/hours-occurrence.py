f = open('mbox-short.txt','r')


count = {}
for line in f:
    if line.startswith('From '):
        line = line.split()
        line = line[5]
        line = line[0:2]
        count[line] = count.get(line, 0 ) + 1

print(count)

# sort = sorted(count.keys())

# print("\n", sort)

# for hrs in count :
#     print(hrs, count[hrs])

print("\n", sorted(count), "\n")

for hrs, cnt in sorted(count.items()) :
    print(hrs, cnt)


f.close()