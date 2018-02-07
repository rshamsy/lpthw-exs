from sys import argv

script, filename = argv

txt = open(filename)
txt_content = txt.read()

print("File contents:\n{}".format(txt_content))

"""
txt_new = input("Type name of file again: ")

txt_new = txt
txt = open(txt)
"""

txt_new_contents = txt.read()


print("{} file contnents:\n{}".format(filename,txt_new_contents))

print("\n Now trying to use readline:")

print("first call of readline: \n{}".format(txt.readline()))
print("second call of readline: \n{}".format(txt.readline()))
print("third call of readline: \n{}".format(txt.readline()))

print("\nTrying readline from within a loop:\n")
for i in range(1,5):
    print(f"line {i}: " + txt.readline(i))

txt.close()
