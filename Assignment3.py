# Swapping using arithmetic operations
a = 5
b = 10

print(f"Before swapping: a = {a}, b = {b}")

a = a + b  # a now becomes 15 (5 + 10)
b = a - b  # b now becomes 5 (15 - 10)
a = a - b  # a now becomes 10 (15 - 5)

print(f"After swapping: a = {a}, b = {b}")
