first = open("input.txt","r")
copy = open("copied.txt","w")
for line in first:
    line = line.swapcase()
    line = line.replace(".",",")
    copy.write(line)
first.close()
copy.close()
