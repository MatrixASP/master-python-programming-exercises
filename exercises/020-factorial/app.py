# Your code here
def factorial(n):
    fct = 1
    while n > 1:
        fct = fct * n
        n -= 1
    return fct

print(factorial(8))
