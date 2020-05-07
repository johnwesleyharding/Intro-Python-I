"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt') as f:
    d = f.read()
    print(d)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

w = open('bar.txt', 'w')
w.write('Needless to say, the spectacle of an individual moving against his or her expert community\n')
w.write('away from carrots and towards sticks is generally viewed as a cause for alarm\n')
w.write('independently of whether that individual is a malfunctioning fool or a genius about to invalidate community groupthink.\n')
w.close()

with open('bar.txt') as f:
    d = f.read()
    print(d)
