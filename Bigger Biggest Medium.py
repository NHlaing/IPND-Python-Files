print('Bigger')

def bigger(a,b):
    return max(a,b)
print(bigger(2,7))
print (bigger(9,6))

print('Biggest')
def biggest(a, b , c):
     return max(a,b,c)
print (biggest(5,6,9))

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
print (biggest(6,5,8))


def biggest(a, b, c):
    return max(a,b,c)
print (biggest(2,5,6))
print (biggest(5,9,13))
print (biggest(11,21,32))


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
print (biggest(6,9,8))




def big(a, b, c):
    return max(a,b,c)

print (big(5,6,4))
print (big(88,54,65))


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
print (big(55,99,66))


print('Median')

def median(a, b ,c):
    if bigger(a, b)<=c:
        return bigger(a,b)
    if bigger(a, c)<=b:
        return bigger(a,c)
    if bigger(c, b)<=a:
        return bigger(c, b)
print (median(5,3,6))
print (median(2,7,9))
print (median(21,52,61))

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def median(a, b, c):
     if bigger(a, b)<=c:
        return bigger(a , b)
     if bigger(a, c)<=b:
        return bigger(a , c)
     if bigger(c, b)<=a:
        return bigger (c , b)
print (median(1,4,8))
print (median(6,9,8))


print('Smaller')
def sma(a, b, c):
    if a <b:
        if a<c:
            return a
        else:
            return c
    else:
        if b <c:
            return b
        else:
            return c
print (sma(1,2,4))
print (sma(2,6,9))
print (sma(51,26,64))
