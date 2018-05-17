from sys import argv

script = argv

filename = open('test.txt')
print(f"I'm going to open file: ".format(filename))
print(filename.read())
