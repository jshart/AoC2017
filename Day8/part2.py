import math


vars = dict()

textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day8\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()

overallMax = 0
for i in input:
    print(i)
    parts = i.split(' ')
    #            0 1   2 3  4 5 6
    # format is; b inc 5 if a > 1

    # first of all lets check to see if the assignment var already exists in the dictionary, or if we need to add it
    if parts[0] in vars:
        print(" |- Var:{} found == {}".format(parts[0], vars[parts[0]]))
    else:
        print(" |- Adding Var:{}".format(parts[0]))
        vars[parts[0]] = 0

    lhs = 0
    # lets next check what LHS value we need to test
    if parts[4] in vars:
        lhs = int(vars[parts[4]])

    rhs = int(parts[6])

    result = False
    # lets check the condition
    if parts[5] == '>':
        if lhs > rhs:
            result = True
    elif parts[5] == '<':
        if lhs < rhs:
            result = True
    elif parts[5] == '>=':
        if lhs >= rhs:
            result = True
    elif parts[5] == '<=':
        if lhs <= rhs:
            result = True
    elif parts[5] == '==':
        if lhs == rhs:
            result = True
    elif parts[5] == '!=':
        if lhs != rhs:
            result = True

    if result:
        if parts[1] == 'inc':
            print(" |- Incrementing {} by {}".format(parts[0], parts[2]))
            vars[parts[0]] += int(parts[2])
        else:
            print(" |- Decrementing {} by {}".format(parts[0], parts[2]))
            vars[parts[0]] -= int(parts[2])
        print(" |- Result: {} == {}".format(parts[0], vars[parts[0]]))

    m = max(vars.values())
    if m > overallMax:
        overallMax = m

for i in vars:
    print(i, vars[i])

print("Max value: {}".format(overallMax))
