def power(a, b):
    result = 1
    base = a 
    exponent = b  

    while exponent > 0:
        result *= base
        exponent -= 1

    return result

a = 2
b = 5
print(power(a, b))
