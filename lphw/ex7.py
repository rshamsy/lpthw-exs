tryString = "x {}"

for i in range(1,10):
    print(tryString.format(i))

tryString_2 = "x"*5
print("\nx*5: " + tryString_2, end=' ')
# ", end=' '" causes the next print statement to coninue on the same line after a space, and not on next line
print("a b c d")
print("\nwith end='':")
print("\nx*5: " + tryString_2, end='')
print("a b c d")
