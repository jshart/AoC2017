
import math

textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day5\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()

ins = list(map(int, input))
done = False
pc = 0
cycles = 0
while not done:
    reg = ins[pc]
    if (reg >= 3):
        ins[pc] -= 1
    else:
        ins[pc] += 1

    pc += reg
    cycles += 1
    if pc >= len(ins):
        done = True

print("Done in %d cycles" % cycles)
#print(ins)
