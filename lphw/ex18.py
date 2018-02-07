def print_two(*args):
    arg1,arg2 = args
    print ("arg1: {}, arg2: {}".format(arg1,arg2))


def print_two_again(arg1,arg2):
    print ("arg1: {}, arg2: {}".format(arg1,arg2))

def print_one(arg1):
    print ("arg1: {}".format(arg1))

def print_none():
    print("nada")

print_two("Rahim","Shamsy")
print_two_again("Rahim","Shamsy")
print_one("One thing")
print_none()
