from sys import argv

script, filename = argv

def print_all(fileobj):
    print(fileobj.read())

def rewindto_beg(fileobj):
    fileobj.seek(0)

def print_a_line(line_count,fileobj):
    print("Line ",line_count,": ",fileobj.readline())

current_file = open(filename)

print("Whole file:\n")

print_all(current_file)

print("must rewind...")
rewindto_beg(current_file)

print("Print 3 lines:\n")

current_line = 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
