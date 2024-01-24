import os

#file = open("C:\\Users\\gottumr0\\pfile.txt", "w")  --- open file in write mode to add content into file.

file = open("C:\\Users\\gottumr0\\p2file.txt", "a")  ## appending mode
file.write("This is a 2nd test.")
file.close()

## Read the content from the file
file = open("C:\\Users\\gottumr0\\p2file.txt", "r")
contents = file.read(6)  ## this will read first 6 char from the file
print(contents)
file.close()

# rename/relocate the file
os.rename("C:\\Users\\gottumr0\\p3file.txt", "C:\\Users\\gottumr0\\p16file.txt")
# Delete the file
os.remove("C:\\Users\\gottumr0\\p4file.txt")