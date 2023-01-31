import math
#1182 too high

class Tree:
    def __init__(self, input):
        self.name = ''
        self.branches = []
        self.w = 0
        self.original_w = 0
        self.parts = input.split(' ')
        self.name = self.parts[0]
        self.w = int(self.parts[1])
        self.original_w = int(self.parts[1])

        for i in range(2, len(self.parts)):
            self.branches.append(self.parts[i])

    def print(self, d, tree):

        print("| " * d, end='')
        print("{} ({})".format(self.name, self.w))

        for branch in self.branches:
            print("| " * d, end='')
            print("+-{}".format(branch))
            for b in tree:
                if branch == b.name:
                    b.print(d + 1, tree)

    def updateWeights(self, tree):
        subTotal = 0
        res = 0
        testWeights = []
        originalWeights = []

        if len(self.branches) > 0:
            # find all sub-branches and calculate their weights
            for branch in self.branches:
                for b in tree:
                    if branch == b.name:
                        res = b.updateWeights(tree)
                        subTotal += res
                        testWeights.append(res)
                        originalWeights.append(b.original_w)

            # check all elements in testWeights to see if they are equal
            for i in range(0, len(testWeights)):
                if testWeights[i] != testWeights[0]:
                    print("ERROR: Branches under [{}]".format(self.name))
                    print("# Have different weights: {}".format(testWeights))
                    print("# Branches:{}".format(self.branches))
                    print("# Original weights: {}".format(originalWeights))
                    break

            self.w += subTotal

        return (self.w)


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day7\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()

tree = []
topTree = None
searchString = 'svugo'
# searchString='tknk'
#searchString = 'oxipms'

for i in input:
    t = Tree(i)
    tree.append(t)
    if t.name == searchString:
        topTree = t

topTree.updateWeights(tree)
#topTree.print(1, tree)
