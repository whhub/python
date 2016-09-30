from sys import argv    # import sys modules

script, filename = argv  # upack argv argument

txt = open(filename)    # open a file in read mode

print("Here's your file %r:" % filename)  # prompt
print(txt.read())                            # read then print the file
txt.close()

print("Type the filename again:")        # prompt
file_again = input('> ')                    # prompt

txt_again = open(file_again)                # open a file

print(txt_again.read())                     # read then print the file
txt_again.close()

