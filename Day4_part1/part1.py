
import math


textfile = open('C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2017\\day4_part1\\data\\input.txt', 'r')
input = textfile.read().split('\n')
#str = open('data\\input.txt', 'r').read()

passwordSet=set()
passwords=0
for i in input:
    setLen=len(passwordSet)
    invalid=False
    
    for k in i.split():
        passwordSet.add(k)
        newSetLen=len(passwordSet)
        
        # if the set didnt grow in size then this password is already in the list
        # as a duplicate it makes the list as a whole illegal
        if newSetLen==setLen:
            invalid=True
        setLen=newSetLen

    if invalid==False:
        passwords+=1
        
    print(passwordSet)
    passwordSet.clear()
    
print(f'Valid passwords:{passwords}')

