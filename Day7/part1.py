import math


class Tree:
    def __init__(self, input):
        self.name = ''
        self.branches = []


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day7\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()

branches = []
leafs = []
for i in input:
    parts = i.split(' ')
    for c, p in enumerate(parts):
        if c == 0:
            branches.append(p)
        if c > 1:
            leafs.append(p)

print("Branches:{}".format(branches))
print("Leafs:{}".format(leafs))

for b in branches:
    if b not in leafs:
        print("Branch {} is not a leaf".format(b))
        break
