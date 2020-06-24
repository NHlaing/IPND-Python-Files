def countdown(number):
    i = number
    while ( i > 0):
        i = i - 1
        print (i)
countdown(3)

def  countdown(n):
        i = 0
        while (i <= n):
            i = i + 1
            print (i)
countdown(2)


def countdown(n):
     i = 1
     while (i <= n):
        print (i)
        i= i+1
countdown(3)



def Big(a, b ,c):
    return max(a,b,c)
print(Big(2,6,1))

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
print(sma(1,2,4))
