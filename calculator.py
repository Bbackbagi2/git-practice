def add(a, b):
    return a + b

print(add(3,4))

def subtract(a, b):
    return a - b

print (subtract(10, 5))

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(10, 2))
print(divide(10, 0))
