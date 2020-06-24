# find_element
### Making with for loops ###
def find_element(list, y):
    i =  0
    for item in list:
        if item == y:
            return i
        i = i + 1
    else:
            return -1
print("(find_element([0,1,2],2))  ====>   " + str(find_element([0,1,2],2)))
print ("(find_element(['alpha','beta'],'gamma')) ====> " + str(find_element(['alpha','beta'],'gamma'))) # User's Answer


def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
           return i
        i = i + 1
    return -1
print(find_element([1,2,3],3))


### Making with while loops ###
def find_element(p,t):
    i = 3
    while i <len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1
print(find_element(['alpha','beta'],'beta')) # .solution

# .index

p = [5,4,2,1]
print(p.index(2))

###  Practice  ###

countries =['China', 'India','Japan','Iran',
            'Indonesia','Vietnam','Thailand',
            'Philippines', 'Hongkong','South Korea']

print(countries.index('Indonesia'))
