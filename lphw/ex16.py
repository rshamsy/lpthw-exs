from sys import argv

# Assume this script's name and file to write to will be passed. But how to create a file within a python script?
script, filename = argv

fileobj = open(filename,'w')

print("Press ENTER if you want to erase {}; CTRL-C otherwise".format(filename))
inPrompt = '>'
print("Enter 3 lines to input now:\n")
line1 = input("Line1:" + inPrompt)
line2 = input("Line2:" + inPrompt)
line3 = input("Line3:" + inPrompt)

print("Erasing file first...")
fileobj.truncate()

print("writing to file...")
fileobj.write(line1)
fileobj.write("\n")
fileobj.write(line2)
fileobj.write("\n")
fileobj.write(line3)
fileobj.write("\n")

fileobj.close()

fileobj = open(filename)
writtenContents = fileobj.read()
print("file contents are as follows\n"  + writtenContents)
