def biggest(a, b, c):
    return max(a,b,c)
print (biggest(2,5,6))
print (biggest(5,9,13))
print (biggest(11,21,32)) # biggest pp


def biggest(a,b,c):
    if a > b:
        if a > c:
           return a
        else:
           return c
    else:
        if b > c:
            return b
        else:
            return c
print (biggest(5,2,6))
print (biggest(6,9,8)) # biggest pp

def big(a, b, c):
    return max(a, b, c)
print (big(5,6,4))
print (big(88,54,65)) # practice


def big(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print (big(9,6,8))
print (big(55,99,66)) # biggest

def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print (biggest(2, 9, 6)) # biggest
