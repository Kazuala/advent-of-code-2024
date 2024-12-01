input = open("input.txt", "r")
list1 = []
list2 = []
total = 0

for lines in input:
    list1.append(lines[:5])
    list2.append(lines[-6:-1])

input.close()

for n in range(len(list1) - 1, 0, -1):
    swapped = False

    for i in range(n):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            swapped = True

    if not swapped:
        break

for n in range(len(list2) - 1, 0, -1):
    swapped = False

    for i in range(n):
        if list2[i] > list2[i + 1]:
            list2[i], list2[i + 1] = list2[i + 1], list2[i]
            swapped = True

    if not swapped:
        break

for n in range(len(list1)):
    if list1[n] > list2[n]:
        total += int(list1[n]) - int(list2[n])
    else:
        total += int(list2[n]) - int(list1[n])

print(total)
