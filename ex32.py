ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not ten things in that list, lets fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There {len(stuff)} items now.")

print("There we go: ", stuff)

print("Lets do something with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
