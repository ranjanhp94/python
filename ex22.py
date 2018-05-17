def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets do some math with just functions!")
age = add(30, 20)
height = subtract(50, 20)
weight = multiply(10, 6)
iq = divide(100, 2)

print(f"Age: {age},Height: {height},Weight: {weight},Iq: {iq}")

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That become:", what, "can you do it by hand?")
