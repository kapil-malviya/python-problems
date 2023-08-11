"""
Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
"""


file = open('mbox-short.txt','r')

count = {}
for line in file:
    if line.startswith('From '):
        line = line.split()
        line = line[5]
        line = line[0:2]
        count[line] = count.get(line, 0 ) + 1

print(count)


print("\n", sorted(count), "\n")
for hrs, cnt in sorted(count.items()) :
    print(hrs, cnt)


file.close()
