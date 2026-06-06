def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *  factorial(n-1) 
    
print(factorial(5))


def fabunacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabunacci(n-1) + fabunacci(n-2)
print(fabunacci(10))
