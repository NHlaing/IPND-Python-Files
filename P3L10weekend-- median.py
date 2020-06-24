def weekend(day):
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False
print (weekend("Monday"))
print (weekend("July"))
print (weekend("Sunday"))


def countdown(number):
    i = number
    while (i>0):
        print(i)
        i-=1
countdown(5)
print ('Blastoff')



def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def median(a, b, c):
    if bigger(a, b)<=c:
        return bigger(a , b)
    if bigger(a, c)<=b:
        return bigger(a, c)
    if bigger(c, b)<=a:
        return bigger (c ,b)
print (median(46,85,123))
