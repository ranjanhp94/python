people = 50
cars = 40
buses = 15

if cars > people:
    print("we should take the cars.")
elif buses < cars:
    print("We should not take the cars.")
else:
    print("We cant decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still cant decide.")

if people > buses:
    print("Alright, lets just take the buses.")
else:
    print("Fine, lets stay home then.")
