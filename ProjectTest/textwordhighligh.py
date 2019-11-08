
##with open("test.txt") as open:
##    for line in open:
##        for part in line.split():
##            if "do" in part:
##                print (part)

file = open('test.txt', 'r')
string = ["do","you"]
lineCount = 0

for x in string:
    print(x + " in: ")
    for line in file:
        print(lineCount)
        lineCount += 1
        if x in line.split(): # remove trailing newline
            print("video" + str(lineCount-1))
    file.seek(0)
    lineCount = 0
