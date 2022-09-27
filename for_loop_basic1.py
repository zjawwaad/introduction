for i in range(151):
    print(i)

##

for i in range(5, 1000, 5):
    print(i)

##

for i in range (1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

# ##
# Add odd integers from 0 to 500,000, and print the final sum.
# for i in range (0,500001):

sum= 0
for i in range(0,500001):
    if (i % 2 != 0):
        sum += i
    if (i >= 500000):
        print(sum)

## 

for i in range (2018,1, -4):
    print(i)



# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only 
# the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 10
mult = 3

for i in range(lowNum,highNum):
    if (i % mult == 0):
        print(i)

