
##with open("test.txt") as open:
##    for line in open:
##        for part in line.split():
##            if "do" in part:
##                print (part)

file = open('test.txt', 'r')
string = ("do")
lineCount = 0
for line in file:
    lineCount += 1
    if string in line.split(): # remove trailing newline
        print("video" + str(lineCount-1))
