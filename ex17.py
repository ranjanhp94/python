from sys import argv
script, filename = argv

print(f"we'r going to erase {filename}.")
print("If you dont want that, hit CTRL+C(^C).")
print("If you you dont want that, hit RETURN.")
input(">")
print("opening the file...")
target = open(filename, 'w')
print("truncating the file.Goodbye!")
target.truncate()

print("Now i'm going to ask you three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write this to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we're going to close it.")
target.close()
