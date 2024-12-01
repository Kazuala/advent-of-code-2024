input = open("input.txt","r")
list1 = []
list2 = []
total = 0

for lines in input:
    list1.append(lines[:5])
    list2.append(lines[-6:-1])

input.close()

for n in range(len(list1)):
    for i in range(len(list2)):
        if list1[n] == list2[i]:
            total += int(list1[n])

print(total)
