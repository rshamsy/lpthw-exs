from sys import argv
from os.path import exists

#write one file's contents to another file, and check the existence of the
#  other file before.

script, file_from, file_to = argv

fromdata = (open(file_from)).read()

print("Does the to-file exist? {}".format(exists(file_to)))

tofile_obj = open(file_to,'w')


tofile_obj.write(fromdata)
(tofile_obj).close()

print("Following are contents of from-file:\n{}".format(fromdata))
print("Following are contents of to-file:\n{}".format(open(file_to).read()))
