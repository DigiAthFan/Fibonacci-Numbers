# Fibonacci Numbers Loop

n = 20

a = 0
b = 1

for i in range(n):
    print(a)
    next = a + b
    a = b
    b = next 
