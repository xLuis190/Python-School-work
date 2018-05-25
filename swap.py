num = int(input())
setA = set()
for x in range(0,num):
    elements = input()
    elements = elements.split(" ")
    for index in range(len(elements)):
        setA.add(int(elements[index]))
print(setA)
setB = set()
num2 = int(input())
for y in range(0,num2):
    elements = input()
    elements = elements.split(" ")
    for index in range(len(elements)):
        setB.add(int(elements[index]))
newSet1 = setA.difference(setB)
newSet2 = setB.difference(setA)
unionSet = newSet1.union(newSet2)
unionSet = sorted(unionSet)
for val in unionSet:
    print(val)
