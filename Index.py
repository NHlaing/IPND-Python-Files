print (".Index")
print('')
p = [5,4,2,1]
print(p.index(2))

###  Practice  ###

countries =['China', 'India','Japan','Iran',
            'Indonesia','Vietnam','Thailand',
            'Philippines', 'Hongkong','South Korea']
print(countries)
print(countries.index('Indonesia'))



def find_element(xlist, y ):
    if y in xlist:
         return xlist.index(y)
    else:
        return -1

print (find_element([1,2,3],3))
print (find_element(['alpha','beta'],'gamma')) # User's Answer



def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1
print (find_element([6,3,1,5,7,8],8))
print (find_element(['a','b','c','d','e'],'e'))  # .solution...


def find_element(p,t):
    if t not in p:
        return -1
    return p.index(t)
print (find_element([6,3,1,5,7,8],1))
print (find_element(['a','b','c','d','e'],'p'))  # .solution...

# ### From Video
# While loops
print ('While loops')
count = 0
while count < 10:
    print (count)
    count +=1

# for loops
print ('For Loops')
L = [1,4,4,3,2,9,0]
for element in L:
    print ("element  ===> " + str(element))

# range

range(50)
for n in range(50):
        print ("Hello! the number is " + str(n))

range(20)
for s in range(20):
    print ("No. +++> " + str(s))
