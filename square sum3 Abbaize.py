def sum(a, b):
    a = a + b
    return a
print (sum(3,6))  # sum procedure with a Rertrurn


def square(n):
    return  n * n
print (square(5))

d = 11
print (square(d))
print (square(square(d)))
y = 121
print (square(y)) # square

def sum3(d,e,f):
    return (d+ e + f)
print (sum3(1,2,3))


def sum3(a,b,c,d):
    return ((a + b) -c) * d

print (sum3(2,18,2,4))

print (sum3(5,4,3,2))

def sum(a,b):
    return a + b
print (sum(6,6))


#    Abbaize

def abbaize(a, b):
    return a + b + a + b
print (abbaize('a', 'b'))
print(abbaize('dog','cat'))
print (abbaize('dog', 'cat'))

def a(a, b):
    return a + b + b + a
print (a('owl', 'crol'))

print(2>3)
print (2*2 !=5)
print (2*2 == 4)

# bigger

def bigger(a,b):
    return max(a,b)
print(bigger(2,7))
print (bigger(9,6))



print('Median')

def median(a, b ,c):
    if bigger(a, b)<=c:
        return bigger(a,b)
    if bigger(a, c)<=b:
        return bigger(a,c)
    if bigger(c, b)<=a:
        return bigger(c, b)
print (median(5,3,6))

  #  Biggest

def Big(a, b ,c):
    return max(a,b,c)
print (Big(2,6,1))



 #  Small

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
